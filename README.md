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

### 2.1. The Template of Doom.

[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_1l91yhag25quxnsxmgaswopagyvq77.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0c6c40ba79057668961e24d64815f9ab19c3c2148b29c9532c6b5a38dcdffa5c63c3e40084d89cc5b1fce062897f99fa0898502297af08)

In **settings.py**, go to _INSTALLED_APPS_ and registered you new app in the list. <br>
Now you can create a _templates_ directory in said application, and in this directory create **index.html**. <br>
In the end if **views.py** you render the index.html when request is sent.

Dynamic data in the template? <br>

1. Send data from our view to our template.
  * create variables in **views.py** request accepting function, and add to context. 
2. Access that data from inside our template.
  * Access a variable from the views context in template using curly braces.
  
 ### 2.2. More Template Fun.
  
[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_1mua59oko6yqy1hbhdd8bjjtvjqiog.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0c6c40bd7362d6654bc1fb9839d76f800194bddef3c9a40f2d3aec86fa86d107f7fdfdf8ef2cce43752c1dc875a6fb8658d01fd1eb556a)

In the case of complicated data display, how to display data in context? <br>
Create a Python class for each object and store all instances in a list, just one we put in context. <br>
Then access this list from the template using _{% for i in list %} and {% endfor %}_.
Also can use, _{% if cond %} {% else %} {% endif %}_.

### 2.3. More Template Fun.
  
[click here for video](https://codeschool-vfs.cdn-ec.viddler.com/codeschool_1pq5qgncesuou18b9i31i1zufl10i2.mp4?fd9f2a1c14aadf1069f046ce61f41e2b05c31bf4bc1c0f4df9c4be0c6c40bf7b353a76c3822546d7a08073db1a053d5de26092f9de712a04e4c84b4f63d0727a31c19cf25f1253d2625045bbc49ad1313d87)

Django looks for directory called static in app directory for CSS, Javascript and static images.<br>
Then in templates add _{% load staticfiles %}_ then add link tag to css file with href _{% static 'style.css' %}_. <br>
You can add third party CSS here, also /images directory for static images.<br>


