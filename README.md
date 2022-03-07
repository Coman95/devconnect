# devconnect
Connect with other developers:

Live demo:
https://connect-w-dev.herokuapp.com/

<br>

Website Features: <br>
Browse and search for developers and projects<br>
Sign up and log in into account + password reset via email<br>
Edit / Delete account information<br>
Create / Edit / Delete your projects<br>
Comment and review other's projects<br>
Send messages to other developers<br>

Technologies Used:<br>
Django<br>
PostgreSQL<br>
JavaScript<br>
HTML / CSS<br>

# Run it yourself
```
git clone https://github.com/Coman95/devconnect.git
cd devsearch
pip install - r requirements.txt
```
Change DB credentials with your own in  ```settings.py``` file
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "devsearch",
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": "5432",
    }
}
```

For Email recovery, change the following with your credentials:
```
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
```

Run migrations: 
```
python manage.py migrate
```
Start app:
```
python manage.py runserver
```
