up:
	docker compose up --build -d

down:
	docker compose down

format:
	docker exec loader python -m black -S --line-length 79 /opt/sde
	docker exec loader isort /opt/sde

type:
	docker exec loader mypy --ignore-missing-imports /opt/sde

lint:
	docker exec loader flake8 /opt/sde

pytest:
	docker exec loader pytest -p no:warnings -v /opt/sde/test

ci: format type lint pytest

run-etl:
	docker exec loader python load_user_data.py

warehouse:
	docker exec -it warehouse psql -U migas