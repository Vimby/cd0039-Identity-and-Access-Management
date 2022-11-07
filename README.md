# cd0039 Identity Access Management
COFFEE SHOP FULL STACK PROJECT

 Coffee Shop is an Udacity full stack project. It is a digitally enabled cafe for students to order drinks, socialize, and study. This projects dwells on setting up their menu experience. The application can
1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.


Completing the coffee shop gives students the ability to aunthenticate and authorize applications using Auth0 and JWT.


GETTING STARTED

Prerequisites and Installation
-This project requires Python3 version, pip and node modules to be installed to your local machine 
-We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


Backend
-From the backend folder run the below to install all dependencies
-The [Backend README](./backend/README.md) contain further details for working on the backend of the project

```bash
pip install -r requirements.txt

```
Running the server
-From within the `./src` directory first ensure you are working using your created virtual environment
export FLASK_APP=api.py

-To run the server, execute:

 flask run --reload

The application is run on http://127.0.0.1:5000/ by default.

Frontend
The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

From the frontend folder, execute the below commands to install the requirements
  npm install #only once to install dependencies

To start the server #This should not be used in production
    ionic serve


```
DEPLOYMENT
N/A

Authors
This project was completed by Vimbai Rusike

ACKNOWLEDGMENTS
The course instructor Gabriel Ruttner and the awesome team at Udacity and our mentors who made this journey easy.
 
