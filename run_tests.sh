safety check &&
python3 -m flake8 --config=unit_tests/.flake8 app/ &&
python3 -m pytest --rootdir=unit_tests/ --cov=app --cov-report=term --cov-report=html --cov-config=unit_tests/.coveragerc unit_tests