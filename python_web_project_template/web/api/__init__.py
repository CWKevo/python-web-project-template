import typing as t
import python_web_project_template.settings as s

from python_web_project_template.private_settings import SENTRY_DSN

import fastapi as fa
from starlette.datastructures import URLPath
from starlette.routing import NoMatchFound

import json
from fastapi.responses import JSONResponse as _JSONResponse

from python_web_project_template.web.api.routers import ALL_ROUTERS



class JSONResponse(_JSONResponse):
    """
        A custom subclass of `JSONResponse` from `fastapi.responses`, that creates JSON responses in a standarized format.
    """

    def render(self, content: t.Any) -> str:
        errors = content.pop('errors', None) if isinstance(content, dict) else None

        _content = {
            'success': errors is None,
            'errors': errors,
            'data': None if errors else content
        }

        return json.dumps(
            _content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")



API = fa.FastAPI(title=s.APP_NAME, version=s.APP_VERSION, docs_url="/", redoc_url="/redoc", default_response_class=JSONResponse)

for router in ALL_ROUTERS:
    API.include_router(router, prefix=router.prefix)



if SENTRY_DSN is not None:
    import sentry_sdk
    from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

    sentry_sdk.init(dsn=SENTRY_DSN)

    API.add_middleware(SentryAsgiMiddleware)



@API.exception_handler(fa.exceptions.RequestValidationError)
async def validation_exception_handler(_, exception: fa.exceptions.RequestValidationError):
    """
        Creates a standarized error response, for consistency accross the API.
    """

    return JSONResponse({"errors": exception.errors()}, status_code=400)



def api_url_for(name: str, as_uri: bool=True, **path_params) -> t.Optional[URLPath]:
    for router in ALL_ROUTERS:
        try:
            route = router.url_path_for(name, **path_params)
            route = f"{API.root_path}{route}"

            if as_uri:
                return route

            else:
                return f"{'https://' if s.USE_HTTPS else 'http://'}{s.API_DOMAIN}{route}"

        except NoMatchFound:
            continue

    raise NoMatchFound
