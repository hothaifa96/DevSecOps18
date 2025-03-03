from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
#    -----http request ----> [{request} ]
#
#
# global list [dish, dish ] <-
app = Flask(__name__)  # flask application
CORS(app)

dishes = [
    {'id': 1,
     'name': "shawarma",
     'price': 39.90,
     'calories': 900}
    ,
    {'id': 2,
     'name': "boreka",
     'price': 19.90,
     'calories': 300}
]

@app.get('/rec/<amount>')
def get_rec(amount):
    amount = int(amount)
    try:
        amount = amount/0
    except Exception as e:
        print(e)
        return 'error',200
    finally:
        print('finally')

    return f"after tax {amount}"

@app.get('/dish')
def get_menu():
    print(request.remote_addr)
    print(request.headers["User-Agent"])
    return jsonify(dishes)


@app.get('/dish/<id>')
def get_dish_by_id(id):
    id = int(id)
    for dish in dishes:
        if dish["id"] == id:
            return jsonify(dish), 203
    return "not found", 404


@app.post('/dish')
def add_dish():
    new_dish = request.json
    if validate_dish(new_dish):
        new_dish['id'] = dishes[-1]["id"] + 1  # len(dishes)+1
        # [{1},{3}]  {4}
        dishes.append(new_dish)
        return 'added', 201
    else:
        print(type(new_dish))
        print(new_dish)
        return 'missing data', 400


@app.delete('/dish/<id>')
def delete_dish_by_id(id):
    id = int(id)
    for dish in dishes:
        if dish["id"] == id:
            dishes.remove(dish)
            return "Done", 200
    return "id not found", 404


@app.put('/dish/<id>')
def update_dish(id):
    id = int(id)
    new_dish = request.json
    new_dish["id"] = id
    for dish in dishes:
        if dish["id"] == id:
            dishes[dishes.index(dish)] = new_dish
            return "Done"
    return "something went wrong", 400
    # [{1},{2},{3},{4}]      {5} /3


def validate_dish(dish):
    if 'price' not in dish.keys() or \
            'name' not in dish.keys() or \
            'calories' not in dish.keys():
        return False
    else:
        return True


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6020)
