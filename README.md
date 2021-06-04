# Challenge 3 Project

## Getting started

The main purpose of this project is to ramp up the owner of this codes with knowledge of Python and to understand core business rules of GHG Sat before 3-4 days starting monday the 31 at 19:00. To do so GHG Sat have sent the [Observation Management](#Challenge3:-Observation-Management) challenge. 

This repository containt a Python project needed to validate minimal knowledge of Python by implemeting basic Rest Api call used to interact with a Shopping cart. The Shopping cart is used for validate the Django feachures.    

## Requirement

### Challenge3: Observation Management

This challenge is very close to what your first mission will look like working at GHGSat. This is thus a very good way for us to assess your skills, and for you to understand the basics of our business. We're looking for your ability to:

 - understand and leverage frameworks (like Django, Flask), libraries (that work with GIS data) and architectures (like REST)
 - create simple and clear solutions to complex problems
 - write maintainable code that others can understand and use


Write a web API (no frontend) in Python3 and Django2+ or Flask and [PostGIS](https://postgis.net/) allowing a user to:

 1. Target: create targets given some co-ordinates (lat/long/elevation) and a name
 2. Observation: create observations of a target given an image file and a timestamp of when the image was captured. You are free to use whatever image and format you want here as a placeholder
 3. Search 1: find all the targets within a given bounding box (co-ordinates for the four corners of a box) and return a list of them
 4. Search 2: find all the observations within a bounding box AND within a specific period of time and return a list of them
 5. Visualization: For search 1 and 2, provide a way to visualize the results, for example generate a KML file suitable for viewing in Google Earth or a page with google maps and an overlay
 
 Please use JSON as the input and output format for all your endpoints

In addition provide the following:

 1. Documentation for how the internals of the system work, how a user would interact with it and how to run it (English or French)
 2. Tests for the API
 3. A Docker container (or docker-compose.yml) that can run the application

## Features

Since the owner did not have enougth time to implement the PostGis Rest API requerements. The following Api call were created as a way of proving Python understanding. The following is the available API:

* GET : Get the content of the shopping cart in Json. Call http://127.0.0.1:8000/cart-items/

* POST : Insert a cart in the database. Call http://127.0.0.1:8000/cart-items/. Json values posted {"product_name":"name","product_price":"41","product_quantity":"1"}

* PATCH : Update a cart item. Call http://127.0.0.1:8000/update-item/1 . Json values posted {"product_quantity":"3"}. The only parameter accepted will be product_quantity

* DELETE : Delete the cart item having a specific Id. Call http://127.0.0.1:8000/update-item/1

In the above examples for PATH and DELETE the id 1 was used (update-item/1). It is better to execute a GET to extract the available Ids. Before executing a PATH and DELETE. The id must exists in the list displayed in the GET output.
Also HTTP status is change depending of the process result.

All the relevent code is in the file shopping_cart/api_app/views.py

PS: Depending of your development environment the port could be different. Also the address 127.0.0.1 is assuming that you are executing this Python project locally on your computer.

## Lessons Learned

* Evalutating Eclipse, PyCharm and VSS code for editing this project (VSC code was used)
* Understanding Python environement and Pip for packages installation
* Understanding the difference between Django and Flask
* Basic understanding of the used of PostGis by reading the Pdf document

## Pitfall

* The first Django PIP installation did not add the django-admin.exe in the Scripts folder of Python.
* Installing Django Rest Framework even if it was not needed by Django to do Rest API call (bezkoder)

## Contributing

- [Naazneen Jatu : Creating a REST API in Python with Django](https://stackabuse.com/creating-a-rest-api-in-python-with-django)

- [bezkoder : Django: POST, PUT, GET, DELETE requests](https://bezkoder.com/django-rest-api/)

- [PostGis PDF Document](https://postgis.net/stuff/postgis-3.1.pdf)

## Licensing

This project is licensed under Unlicense license. This license does not require
you to take the license with you to your project.