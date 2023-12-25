all:
	python -m PyInstaller -F transcript.py
	move /y dist\transcript.exe transcript.exe
	del /F /Q transcript.spec
	rmdir /S /Q build
	rmdir dist

clean:
	del /F /Q transcript.exe
