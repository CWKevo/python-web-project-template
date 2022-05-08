import typing as t

import python_web_project_template.settings as s

from flask import Flask
from flask_login import LoginManager
from flask_babel import Babel

from sqlmodel import Session, select

from python_web_project_template.database import DATABASE
from python_web_project_template.database.models import User

from python_web_project_template.web.api import api_url_for
from python_web_project_template.web.blueprints import ALL_BLUEPRINTS

from python_web_project_template.private_settings import SENTRY_DSN, SECRET_KEY # type: ignore


if SENTRY_DSN is not None:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[FlaskIntegration()], traces_sample_rate=1.0)


WEB = Flask(__name__)
WEB.config["SECRET_KEY"] = SECRET_KEY
WEB.config['DEBUG'] = s.DEBUG
WEB.config['BABEL_TRANSLATION_DIRECTORIES'] = '../localization/translations'

AUTHENTICATION = LoginManager(WEB)
BABEL = Babel(WEB)

for blueprint in ALL_BLUEPRINTS:
    WEB.register_blueprint(blueprint)



@WEB.context_processor
def add_additional_context():
    return {
        'api_url_for': api_url_for,
        'APP_NAME': s.APP_NAME,
        'APP_VERSION': s.APP_VERSION
    }



@AUTHENTICATION.user_loader
def load_user(id) -> t.Optional[User]:
    with Session(DATABASE) as session:
        return session.exec(select(User).where(User.id == id)).first()



if __name__ == '__main__':
    WEB.run(host=s.WEB_HOST, port=s.WEB_PORT, debug=s.DEBUG)
