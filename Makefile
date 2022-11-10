lint:
	black --check .
	pylint ./**/*.py
	
fix:
	black .
