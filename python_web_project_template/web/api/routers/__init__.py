import typing as t

from fastapi import APIRouter

from python_web_project_template.web.api.routers.main import MAIN_ROUTER


ALL_ROUTERS: t.List[t.Type[APIRouter]] = [
    MAIN_ROUTER
]
