# Django
## Django Tutorial: Code School

### 1.1. What is Django?

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_qmghkogqmzexflm8g5vb94a1746maq.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0c6c40b879e1ac5b0c3da0899bd63d11f95e1bbb52a5bfda99eec8cc026c03d1bc41b7152d7a94041b9df6d63ff0b4beab8c044c351a1e)

> django-admin startproject Treasuregram

**settings.py** holds the project settings.
**urls.py** holds our project's URL's.
**manage.py** is a utility for administrative tasks.

> python manage.py runserver

> python manage.py startapp main_app

**views.py** Python function that takes in a web request and returns a web response.
Define you function here then reflect it in **urls.py** which is a URL dispatcher.
Tie it to main_app with **_from main_app import views_**.

### 1.2. URL Dispatcher - Best practices

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_6d6na606z78x1mxc7l0hfx8gu1t9zg.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0c6c40b879e1a95b0c3da0899b104c87835e93bfd4dd1e5eb02376dc59d11a52e9fe9988bd6350f98589e4611d8c06bc94c8fae1ad23a2)

  * Homepage should be displayed without route.
  * Distinguish between **Project** and **App** URL dispatcher, by creating urls.py to each app in project.
  * 