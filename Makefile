all: clean
	python -m PyInstaller transcript.py

clean:
	powershell -Command 'Remove-ItemSafely dist'