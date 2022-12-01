lint:
	black --check .
	pylint ./**/*.py
	
fix:
	black .

build:
	docker-compose up --build -d

up-no-build:
	docker-compose up -d

run-charge:
	docker-compose -f docker-compose.yml run srbarriga python3 app/main.py