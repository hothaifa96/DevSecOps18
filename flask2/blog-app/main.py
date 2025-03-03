import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from post import Post

# declare flaks app for @
app = Flask("BolgBIU")
# cors allow all requests to get to the be
CORS(app)


def generate_posts():
    po = [Post(1, 'greet', 'dani', '<3 <3 <3', '11/12'),
          Post(2, 'welcome', 'yossi', 'wel wel welcome', '11/12'),
          Post(3, 'how to get in shape in 5 min', 'malkom', 'posts and post ', '11/12')]
    return po


# posts
posts = generate_posts()


# get all
@app.get('/posts')
def get_all_posts():
    try:
        res = [post.__dict__ for post in posts]
        response = {"status": True, "posts": res}
    except Exception as e:
        response = {"status": False, "message": e}
    return jsonify(response)


# get by id
@app.get('/posts/<id>')
def get_post_by_id(id):
    for post in posts:
        if post.id == id:
            return jsonify(post.__dict__)
    return {"success": False, "message": "id not found"}


# add post
@app.post('/posts')
def add_new_post():
    data = request.json
    new_post = Post(data['id'], data['title'], data['author'], data['content'], datetime.datetime.now())
    for post in posts:
        if post.id == new_post.id:
            return {"success": False, "message": "post id already exists"} ,400
    posts.append(new_post)
    return jsonify({
        "success": True,
        "message": "Post created successfully",
        "post": new_post.__dict__})


# update post

# delete post
@app.delete('/posts/<id>')
def delete_user(id):
    id = int(id)
    for post in posts:
        if post.id == id:
            posts.remove(post)
            return {"success": True, "message": f"user {id} deleted"}, 200
    return {"success": False, "message": f"user {id} not found"}, 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
