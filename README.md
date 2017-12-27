# Catalog Application

Catalog application is a RESTful web application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items. This application also provides a few JSON endpoints.


# Running and setup

The server code for the application is written in python and makes use of the 'flask' frame-work to handle http requests. The application also uses 'sqlalchemy' which is an ORM for python to connect to an 'sqlite' database. To run the server code for this application the server will need to have to above mention frame-works installed. To start the server code for the application, run the python file ``` project.py``` using the following command if you want to directly use the existing sqlite database.
```sh
$ python project.py
``` 
The application will run on ```localhost:5000```. If you want to create a new database, delete the ```catalogmenu.db``` file and create a new database by running ```database_setup1.py``` using the following command
```sh
$ python database_setup1.py
``` 
To generate the initial item in the entries in the database, please run the python file ```generatemenus.py``` which will generate the initial entries for the database.
Also make sure that the ```client_secrets.json``` file is in the same folder as the ```project.py``` file
### JSON End points

This application also has a few RESTful web API end points that return data in JSON format. The is a request that will give the all the categories present in the database. The example request for that is:
```http://localhost:5000/category/JSON``` 
For which an example output would be something as:
```
{
  "category": [
    {
      "name": "Guitars", 
      "id": 1
    }, 
    {
      "name": "Keyboards", 
      "id": 2
    }, 
    {
      "name": "Violins", 
      "id": 3
    }, 
    {
      "name": "Precussion", 
      "id": 4
    }
  ]
}
```
There is also a request that will give the menu for the individual categories. The request is as follows:
```http://localhost:5000/category/<int:category_id>/menu/JSON``` where ```category_id``` is the id for the particular category in the database. An example request would be as follows:
```http://localhost:5000/category/1/menu/JSON```
An example output would be:
```
{
  "CategoryMenu": [
    {
      "name": "Acoustic Guitars", 
      "description": "An acoustic guitar is a guitar that produces sound acoustically\u2014by transmitting the vibration of the strings to the air\u2014as opposed to relying on electronic amplification."
    }, 
    {
      "name": "Electric Guitars", 
      "description": "An electric guitar is a fretted stringed instrument with a neck and body that uses a pickup to convert the vibration of its strings into electrical signals."
    }, 
    {
      "name": "Acoustic-Electric Guitars", 
      "description": "An acoustic-electric guitar (also called an electro-acoustic guitar) is an acoustic guitar fitted with a magnetic pickup, a piezoelectric pickup or a microphone."
    }
  ]
}
```
There is also a request that will the individual item of a menu for an individual category. The request is as follows:
```http://localhost:5000/category/<int:category_id>/menu/<int:menu_id>/JSON``` where ```category_id``` is the id for a particular category in the database and ```menu_id``` is the id for a particular item in the database.
An example request would be as follows:
```http://localhost:5000/category/1/menu/1/JSON```
The example output for this would be:
```
{
  "Menu_Item": {
    "name": "Acoustic Guitars", 
    "description": "An acoustic guitar is a guitar that produces sound acoustically\u2014by transmitting the vibration of the strings to the air\u2014as opposed to relying on electronic amplification."
  }
}
```