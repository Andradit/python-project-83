install:
	pipx install uv

build:
	uv build

publish:
	uv publish --dry-run

package-install:
	pipx install --force --include-deps dist/*.whl

dev:
	uv run flask --debug --app page_analyzer:app run

PORT ?= 8000
start:
	psql -a -d $$DATABASE_URL -f database.sql
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app