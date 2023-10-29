.PHONY: help dev pipfreeze history revision upgrade downgrade

help:
	@echo "Available targets:"
	@echo "  dev            : Start the development server."
	@echo "  db            : "Connect mysql database."
	@echo "  history        : Show the migration history."
	@echo "  revision m=<message>  : Create a new migration file with the specified message."
	@echo "  upgrade v=<version>   : Upgrade the database to the specified version (default: head)."
	@echo "  downgrade v=<version> : Downgrade the database to the specified version."

dev:
	@echo "Starting development server..."
	@uvicorn app.main:app --reload

db:
	@PGPASSWORD=$(PGPASSWORD) psql $(PGDATABASE) -U $(PGUSER)

history:
	@alembic history

revision:
	@echo "Creating migration file..."
	@alembic revision --autogenerate -m "$(m)"

upgrade:
	@if [ -n "$(v)" ]; then \
		alembic upgrade $(v); \
	else \
		alembic upgrade head; \
	fi

# 初期状態に戻すためは、`make downgrade v=base` とする
# 一つ前のバージョンに戻したい場合には、`make downgrade v=-1` とする
downgrade:
	@alembic downgrade $(v)

# 開発環境下では、マイグレーションファイルをむやみに作成しないようにする
resetmigrations:
	@alembic downgrade base
	@PGPASSWORD=$(PGPASSWORD) psql $(PGDATABASE) -U $(PGUSER) -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
	@rm -rf ./alembic/versions/*
	@alembic revision --autogenerate -m "init"
	@alembic upgrade head

seed:
	@curl -X POST http://127.0.0.1:8000/seeder

# devcontainerを使っていない人用
# format:
# 	@black --line-length 120 app/*
