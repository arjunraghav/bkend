Follow the instructions

To install dependencies:
copy unzip bkend.zip or
pip install virtualenv
python -m venv .venv
pip install -r requirements.txt
.\.venv\Scripts\activate

Api urls:
Login url - 'http://127.0.0.1:8000/mylogin/'
File upload url - 'http://127.0.0.1:8000/upload/'

Login uses session authentication hence go to 'http://127.0.0.1:8000/mylogin/' and on successful login view automatically redirects to File upload url - 'http://127.0.0.1:8000/upload/'

Uploading the files will give upload id and is limited to 5 uploads.
