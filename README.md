# DevJobApi

Programming job listing api

[![Programming Language](https://img.shields.io/badge/Language-Python-success?style=flat-square)](https://python.org)
[![Framework](https://img.shields.io/badge/Framework-Django%20Rest-success?style=flat-square)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-success.svg?style=flat-square)](https://github.com/Mastersam07/devjobapi/blob/main/LICENSE)

> Please note that i am in no way related to any of the jobs/company listed by this api. All jobs are gotten from the following via an automated process:
>> - https://weworkremotely.com/
>> - https://remoteok.io/remote-dev-jobs
>> - https://www.employremotely.com/jobs
<!-- >>https://remotive.io/remote-jobs/software-dev -->
>> - https://stackoverflow.com/jobs
>> - https://jobs.github.com
>> - https://remote.co/remote-jobs/developer
>> - https://www.python.org/jobs
>> - https://www.hackerrank.com/jobs/search


## 💻 Requirements
* Any Operating System (ie. MacOS X, Linux, Windows)
* Any IDE with python installed on your system(ie. Pycharm, VSCode etc)
* A little knowledge of Python, Django and Web scrapping
* Hands to code and a brain to think 🤓

## ✨ Features
- [x] View All Jobs
- [x] Apply for job
- [x] Save Jobs
- [x] View All Saved Jobs


## Dependencies
* [Django](https://flutter.dev/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [PostgreSql](https://www.postgresql.org/)

## Docs
- [Swagger Docs](http://devjobhub.herokuapp.com/api/v1/swagger)

## Getting started

#### 1. [Setting up PostgreSql](https://www.postgresql.org/)

#### 2. Clone the repo

```sh
$ git clone https://github.com/Mastersam07/devjobapi.git
$ cd devjobapi
```

#### 3. [Setup a virtual environment](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)

#### 4. Get requirements

```sh
$ pip install requirements.txt
```

#### 5. Migrate database
 
```sh
$ cd ..\api
$ python manage.py migrate
```

#### 6. Get the data

```sh
$ python manage.py scrape
```

#### 7. Run the application

```sh
$ python manage.py runserver
```

#### 8. Run the application in deployment(debug: false)

* ##### Create the folder "static" in the project root directory
* ##### Add the below bit of code to settings.py

```sh
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
* ##### Run the below command in your terminal
```sh
$ python manage.py collectstatic
```
* ##### Your project is now production ready

## 📸 ScreenShots


## 📊📈📉

## :heart: Found this project useful?
#### If you found this project useful or you like what you see, then please consider giving it a :star: on Github and sharing it with your friends via social media.

## 🐛 Bugs/Request
#### Encounter any problem(s)? feel free to open an issue. If you feel you could make something better, please raise a ticket on Github and I'll look into it. Pull request are also welcome.

## Credits
- [DevJobHub](https://github.com/LordGhostX/devjobhub) by [LordGhostX](https://github.com/LordGhostX)

## ⭐️ License
#### <a href="https://github.com/Mastersam07/devjobapi/blob/master/LICENSE">MIT LICENSE</a>

## 🤓 Developer(s)
#### **Abada Samuel Oghenero**
<a href="https://twitter.com/mastersam_"><img src="https://github.com/aritraroy/social-icons/blob/master/twitter-icon.png?raw=true" width="60"></a>
<a href="https://linkedin.com/in/abada-samuel/"><img src="https://github.com/aritraroy/social-icons/blob/master/linkedin-icon.png?raw=true" width="60"></a>
<a href="https://medium.com/@sammytech"><img src="https://github.com/aritraroy/social-icons/blob/master/medium-icon.png?raw=true" width="60"></a>
<a href="https://facebook.com/abada.samueloghenero"><img src="https://github.com/aritraroy/social-icons/blob/master/facebook-icon.png?raw=true" width="60"></a>

