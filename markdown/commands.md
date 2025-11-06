# Django Commands

## 初始
```shell
python3 -m venv venv/points_reward_api
```
```shell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\points_reward_api\Scripts\activate
pip install django
pip install djangorestframework
```
```shell
django-admin startproject points_reward_api
mv points_reward_api src
```
```shell
cd src
python manage.py migrate
python manage.py runserver
```
```shell
python manage.py createsuperuser
```
## 功能新增
```shell
python manage.py startapp core
```
```shell
python manage.py makemigrations
python manage.py migrate
```