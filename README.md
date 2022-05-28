# APPLICANT-REPOSITORY
BSIT 2-5 GITHUB

AFTER DOWNLOADING

OPEN XAMPP
START MYAPACHE AND MYSQL

create plm_trialdb database 

pwedeng sa cmd or dito -->> localhost/phpmyadmin tas may new dun tas create database na iyon

Much better if your using visual studio code to follow the following instructions

**1 Create virtual environment**
`python -m venv env`

**2 Activate virtual env.**
Bash : `$ source ./env/Scripts/Activate`
CMD : `env\Scripts\Activate.bat` or by simply typing `env`
if not working:
try this -->>  .\env\Scripts\Activate.ps1


**3 Install dependencies**
`pip install -r requirements.txt`

**3.5 SEARCH IN VS CODE**

open views.py 

search select last_insert

then lahat ng may a = cursor lagyan ng # sa tabi ni a
ganto kalalabasan

#a = cursor

tapos sa taas ng if b == 1: lagay kayo ng a = 1
ganto lalabas

a = 1
if b == 1:

then save views.py


**4 Make Migrations**
`python manage.py makemigrations`

**5 Migrate**
`python manage.py migrate`

**6 Statics**
`py manage.py collectstatic` then type `yes`

**7 Create Admin**
`python manage.py createsuperuser`

> Sample <br>
> Email: admin@plm.edu.ph <br>
> First name: Admin <br>
> Middle name: Admin <br>
> Last name: Admin <br>
> Password: Abc_1234 (Type lang kayo kahit di visible) <br>
> Password (again): Abc_1234 <br>

_Optional_
**NOTE: Pwede mo lang ito magamit pag fresh pa ang database mo (Walang laman)**
You can run `python manage.py databaseseed` to add users with default password of `password`

** 7.5 delete comments**
open views.py 

search select last_insert

tanggalin yung # sa tabi ng a at idelete yung a = 1

**8 Runserver**
`python manage.py runserver` then **Ctrl+click 127.0.0.1:8000**
<br> or you can simply type `run` then hit enter then paste this link `localhost:8000` in your browser to access the iPLM website.

If may problem or questions just pm Joey Lauriaga

Thank you. 


NOTE: IBA PA ITO SA FINAL REPOSITORY OR FINAL CODE NG iPLM. This repository is for BSIT 2-5 only.
