Setup

git clone <repo>
cd social_media_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Endpoints

Endpoint	Method	Description
/api/register/	POST	Register user
/api/login/	POST	Login user
/api/profile/	GET	User profile

Authentication uses Token Authentication.