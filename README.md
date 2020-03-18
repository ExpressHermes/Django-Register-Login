# Django-Register-Login

## Prerequisites
* Python 3
* Django

### Password Hashers used in this app
* Argon2
* Bcrypt


## How to start

 Following commands are for linux. Please google their windows alternative

* Clone the repo on your machine.
* Setup a virtual environment for python3 using command:
```
python3 -m venv myvenv
```
* Activate your virtual environment using command:
 ```
 source venv/bin/activate
 ```
### Install Requirements
 ```
 pip install django
 pip install bcrypt
 pip install django[argon2]

 ```
 
 * Copy the InternTask folder in your directory containing myvenv
 * Inside InternTask folder, in terminal type:
 ```
 python manage.py runserver

 ```
 
 Your server will at http://localhost:[port-number]/
 
 * Go to the port shown in your terminal to see your app
 
 #### Super User 
 To check the registered users, create super user using given command and login to admin page.
 ```
 python manage.py createsuperuser
 ```
 
 
 
