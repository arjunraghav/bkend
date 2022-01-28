README INSTRUCTIONS

Follow the instructions below

To install dependencies:

1. unzip bkend.zip downloeded from github link:'https://github.com/arjunraghav/bkend.git' or run this command in powershell 'git clone https://github.com/arjunraghav/bkend.git'
2. open power shell and navigate inside the bkend dir and run below commands
3. pip install virtualenv
4. python -m venv .venv
5. .\.venv\Scripts\activate
6. pip install -r requirements.txt
7. navigate to django project root ie, same level as manage.py and run 'python manage.py runserver' and wait for console to display 'Starting development server at http://127.0.0.1:8000/'

After starting local dev server follow below urls to validate:

Api urls:
Login url - 'http://127.0.0.1:8000/mylogin/'
File upload url - 'http://127.0.0.1:8000/upload/'

Login uses session authentication hence go to 'http://127.0.0.1:8000/mylogin/' and on successful login view automatically redirects to File upload url - 'http://127.0.0.1:8000/upload/'

Uploading the files will give upload id and is limited to 5 uploads.
