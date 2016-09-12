install:
	@pip install pytest

clean:
	@find . -name "*.pyc" -o -name ".cache" -o -name "__pycache__" | xargs rm -rf
