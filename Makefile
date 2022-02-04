push_to_test:
	poetry build
	poetry publish -r testpypi
