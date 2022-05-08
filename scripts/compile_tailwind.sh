cd "$(dirname "$0")/.."
cd tailwind

npx tailwindcss -i ../python_web_project_template/web/static/css/tailwind_base.css -o ../python_web_project_template/web/static/css/production.css
npx cleancss ../python_web_project_template/web/static/css/production.css -o ../python_web_project_template/web/static/css/production.min.css

rm ../python_web_project_template/web/static/css/production.css
