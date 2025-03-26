from flask import Flask, request

app = Flask(__name__)

movies = [
    {"id": 1, "name": 'spider man 3', 'length': 139, 'genre': 'sci-fi'},
    {"id": 2, "name": 'undisputed', 'length': 110, 'genre': 'action'},
]

# GET -> return all the movies
@app.get('/movie')
def get_all_movies():
    '''
    this function return all the movies
    '''
    return movies


# GET /id -> return one movie
@app.get('/movie/<int:id>')
def get_movie(id):
    '''
    :param id:  movie id
    :return: the movie dict
    '''
    for movie in movies:
        if movie['id'] == id:
            return movie
    return 'data not found', 400  # return message/data , status code


# POST -> add movie to the list

@app.post('/movie')
def add_movie():
    movie = request.json  # takes the body and convert the json to dict
    movie['id'] = movies[-1]['id'] + 1
    # validation
    movies.append(movie)
    return movies


# put -> change movie
@app.put('/movie/<int:id>')
def change_movie(id):
    new_movie = request.json  # take the new movie from the body of the request
    for i in range(len(movies)):  # iterate over all the movies indexes
        if movies[i]['id'] == id:  # if the id of the movie matches the param id
            movies.pop(i)  # remove the old movie
            movies.insert(i, new_movie)  # add new movie
    return 'DoDO'


# delete -> remove all the movies
@app.delete('/movie')
def delete_all_movies():
    movies.clear()
    return movies


# delete /id -> delete one movie
@app.delete('/movie/<int:id>')
def delete_movie(id):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
    return 'Done'



app.run(port=3030,host='0.0.0.0',use_reloader=True)







