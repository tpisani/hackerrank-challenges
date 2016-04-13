install:
	@pip install pytest

clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf
