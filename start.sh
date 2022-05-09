cd "$(dirname "$0")"

export FLASK_APP="python_web_project_template.web:WEB"

(flask run --host 0.0.0.0 --port 5000 & uvicorn python_web_project_template.web.api:API --host 0.0.0.0 --port 5001)
