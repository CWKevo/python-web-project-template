cd "$(dirname "$0")"

export FLASK_APP="python_web_project_template.web:WEB"

# XXX: Ctrl+C will only terminate Uvicorn, Flask will keep running in the background (Windows, Git Bash). If you know a way around this, please make a PR, thanks!
flask run --host 0.0.0.0 --port 5000 & uvicorn python_web_project_template.web.api:API --host 0.0.0.0 --port 5001
