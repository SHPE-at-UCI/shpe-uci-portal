echo "Creating virtual env"
py -3 -m venv venv 

echo "Activating venv"
<<<<<<< HEAD
venv\Scripts\activate & echo "Installing Dependencies" & pip3 install -r requirements.txt & deactivate
=======
venv\Scripts\activate & echo "Installing Dependencies" & pip3 install -r requirements.txt & pip install -r install-pyrebase.txt & deactivate
>>>>>>> 5f38ff12eeeae4d1a9b9c6cf5d54b9e28f8ba3a6

echo "Finished! Now run runapp-windows.bat"

