# ProductHunt-Clone-Django
This is a clone of the Product Hunt website(https://www.producthunt.com) made using Django, Bootstrap 4 and JavaScript.
PostgreSQl has been used as Database for this project.
## Overview

This web application creates an online catalog for some products, where users can browse available products, upvote them, downvote them,add new products and manage their accounts with fully functional authentication system.

The main features that have currently been implemented are:

* There are models for products and users.
* Users can view list and detail information for products.
* Logged In Users can create, view and upvote models.
* Admin(Superuser) users can create and manage models.

## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
I recommend using a Python virtual environment or you can use pipenv for less hassle.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):

pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser # Create a superuser
python3 manage.py runserver
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
2. Create a few test products to see the site in action.
3. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.

Enjoy!! :)
