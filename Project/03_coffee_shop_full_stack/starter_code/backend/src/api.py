import os
import sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
 
#db_drop_and_create_all()
# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
#GET DRINKS ENDPOINT
@app.route("/drinks")
def get_short_drinks():
  drinks = Drink.query.all()
  print(drinks)
  return jsonify({
        "success": True,
        "drinks": [drink.short() for drink in drinks]
    }), 200

  

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
#GET DRINKS DETAILS ENDPOINT
@app.route("/drinks-detail")
@requires_auth("get:drinks-detail")
def get_drinks_detail(payload):
  drinks = Drink.query.all()
  return jsonify({
        "success": True,
        "drinks": [drink.long() for drink in drinks]
    }), 200
  

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
#POST DRINKS ENDPOINT
@app.route("/drinks", methods=["POST"])
@requires_auth("post:drinks")
def post_drink(payload):
    data = request.get_json()

    req_title = data.get("title", None)
    req_recipe = json.dumps(data.get('recipe', None))

    try:
          drink = Drink(title=req_title, recipe=req_recipe)
    
          drink.insert()
          print(sys.exc_info())
     
          return jsonify({
        "success": True,
        "drinks": [drink.long()]
    }), 200

    except:
            print(sys.exc_info())
            abort(422)

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
#PATCH DRINKS ENDPOINT
@app.route("/drinks/<int:id>", methods=['PATCH'])
@requires_auth("patch:drinks")
def update_drink(payload, id):
    drink = Drink.query.get(id)
    if drink is None:
        abort(404)

    data = request.get_json()
    if 'title' in data:
        drink.title = data['title']

    if 'recipe' in data:
        drink.recipe = json.dumps(data['recipe'])

    drink.update()

    return jsonify({
        "success": True,
        "drinks": [drink.long()]
    })
'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

#DELETE DRINKS ENDPOINT
@app.route("/drinks/<int:drink_id>", methods=['DELETE'])
@requires_auth("delete:drinks")
def delete_drinks(payload,drink_id):
      try:
        drink = Drink.query.get(drink_id)

        if drink is None:
            abort (404)

        drink.delete()
        
        return jsonify({
                "success": True,
                 "deleted": drink_id
            }, 200)
    
      except:
        print(sys.exc_info())
        abort(422)
    

# ERROR HANDLING
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found(error):
     return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def handle_auth_error(err):  
     return jsonify({
        "success": False, 
        "error": err,
        "status_code": err.status_code,
        "message": err.description
        }, err.status_code)
  




