echo "Creating virtual env"
py -3 -m venv venv 

echo "Activating venv"
venv\Scripts\activate & echo "Installing Dependencies" & pip3 install -r requirements.txt & pip install -r install-pyrebase.txt & deactivate

echo "Finished! Now run runapp-windows.bat"

