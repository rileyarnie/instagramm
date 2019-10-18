# instagram

#### This is a python-django app that mimicks instagram.

By: Arnold Kibira

## Description
This is a web-app that mimicks the instagram web app and allows users to see images displayed and can click on the image to see more details like the comments.


As of this being published, there are only 3 categories a user can search by: 
- Heroes
- Food
- Cars

There are plans to populate the database more.

## User Story
- A user can create an account, login and use the app
- A user recieves a confirmation email upon registration
- A user can view photos
- A user can see more details of the photos.
- A user can search for profiles by name.
- A user can see the details of the photos selected/clicked on.
- A user can be able to like a photo


### Prerequisites
The following are required to run this apllication and provided are the downoad links and instructions to install them

- Python
  Link:-> ```https://www.python.org/downloads/```
- Django
   Link:-> ```https://www.djangoproject.com/```
- PSQL
  Link:-> ```https://www.postgresql.org/```   
- Heroku
   Link:-> ```https://devcenter.heroku.com/articles/heroku-cli```
- Gunicorn
   Link:-> ```https://docs.gunicorn.org/en/stable/install.html```
   
   
   
## Setup/Installation Requirements
*   Fork the repository
*   git clone the project to your local machine
*   Set up a virtual environment in the project folder
```
python3.6 -m venv --without-pip virtual
```
*   Provided on the link description is the live link to the deployed 
```
https://iinnsstagramm.herokuapp.com/
```

## Known Bugs
* Whenenever a user likes a post the page reloads and the user has to click on the image details to see the like
* Clicking on a user's profile name doesn't redirect you to their profile
* Comments are not displayed under the image but on the image detail page.



## App Screenshots
<ol>
<li>Registration Page <img src="https://github.com/rileyarnie/instagram/blob/master/media/screenshots/register.png" width=1000; alt="My cool logo"></li>
<li>Login page<img src="https://github.com/rileyarnie/instagram/blob/master/media/screenshots/instalogin.png" width=1000; alt="My cool logo"></li>
<li>Home details<img src="https://github.com/rileyarnie/instagram/blob/master/media/screenshots/homepageinsta.png" width=1000; alt="My cool logo"></li>
<li>Commenting <img src="https://github.com/rileyarnie/instagram/blob/master/media/screenshots/comment.png" width=1000; alt="My cool logo"></li>
<li>Comment posted <img src="https://github.com/rileyarnie/instagram/blob/master/media/screenshots/commentposted.png" width=1000; alt="My cool logo"></li>
<li>Delete Comment <img src="https://github.com/rileyarnie/instagram/blob/master/media/screenshots/delete.png" width=1000; alt="My cool logo"></li>


</ol>

## Author
Arnold Kibira

### Technologies Used
* Python3.6
* HTML
* Django Web Framework
* MDBootstrap 

## Licence
 
 [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)


 Copyright (c) 2019 ArnoldKibira


   
