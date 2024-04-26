upload: # https://pypi.org/manage/account/token/ 
	twine upload dist/*

release: clean build-pkg upload clean
	@echo "Sending to PyPI..."

build-pkg: clean
	@echo "Building package"
	python -m pip install build twine
	python -m build

clean:
	@echo "Cleaning files"
	@rm -rf build/ dist/ *.egg-info/ __pycache__/
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@echo "Cleaning finished"