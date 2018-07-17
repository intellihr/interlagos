run:
	while : ; do sleep 2073600 ; done

test:
	flake8 --exclude='tests/snapshots/*' . && python -m pytest tests
