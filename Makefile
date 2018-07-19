run:
	while : ; do sleep 2073600 ; done

test:
	flake8 --exclude='tests/**/snapshots/*,**/__version__.py' . && python -m pytest tests

release:
	python setup.py sdist release
