.PHONY: clean dist upload deploy

clean:
	rm -rf build/ dist/ *.egg-info

dist: clean
	python setup.py sdist bdist_wheel

upload:
	source .env && twine upload dist/*

deploy: dist upload
	rm -rf dist/
