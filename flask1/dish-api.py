from flask import Flask, jsonify, request

#    -----http request ----> [{request} ]
#
#
# global list [dish, dish ] <-
app = Flask(__name__)  # flask application


dishes = [
    {'id': 1,
     'name': "shawarma",
     'price': 39.90,
     'calories': 900}
    , {'id': 2,
       'name': "boreka",
       'price': 19.90,
       'calories': 300}
]


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
        new_dish['id'] = len(dishes) + 1
        dishes.append(new_dish)
        return 'added', 201
    else:
        print(type(new_dish))
        print(new_dish)
        return 'missing data',400




def validate_dish(dish):
    if 'price' not in dish.keys() or\
            'name' not in dish.keys() or\
            'calories' not in dish.keys() :
        return False
    else:
        return True


if __name__ == '__main__':
    app.run(port=6020)
