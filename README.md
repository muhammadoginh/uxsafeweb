## Run Flask UxSAFE

### 1. Get the code
    git clone https://github.com/muhammadoginh/uxsafeweb.git
    cd uxsafeweb

### 2. Install requirements 
    pip install -r requirements.txt

### 3. Set the FLASK_APP environment variable
    (Windows) set FLASK_APP=uxsafe.py
    (Unix) export FLASK_APP=uxsafe.py
    (Powershell) $env:FLASK_APP = ".\uxsafe.py"

### 4. Run the application
    flask run --host=0.0.0.0 --> running on private IP
    flask run --> running on localhost

### 4. Go to http://server_address:5000/, log in using admin admin
