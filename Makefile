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
	python3 app/charger.py

run-payment:
	python3 app/payment.py 