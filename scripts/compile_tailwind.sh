cd "$(dirname "$0")/.."
cd tailwind

npx tailwindcss -i ../python_web_project_template/web/static/css/tailwind_base.css -o ../poznamkovac/web/staticke_subory/css/production.css
npx cleancss -o ../python_web_project_template/web/static/css/production.min.css ../poznamkovac/web/staticke_subory/css/production.css

rm ../python_web_project_template/web/static/css/production.css
