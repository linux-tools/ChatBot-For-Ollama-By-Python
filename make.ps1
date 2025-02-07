echo "Starting installation of dependencies..."
pip install -r requirements.txt
python -m nuitka --windows-console-mode="disable" --enable-plugins="pyside6" --standalone --onefile --show-progress --msvc="latest" --output-dir=output main.py --follow-imports --windows-icon-from-ico=ChatBot_For_Ollama.ico --output-filename="ChatBot_For_Ollama.exe"