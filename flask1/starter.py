from flask import Flask

app = Flask(__name__)  # main


@app.get('/')
def home_page():
    return 'hello world , from flask'


@app.get('/mama')
def greet():
    return 'hello habibi you are in mama section '


@app.get('/home')
def home():
    return ' <h2 style="color:red;" class="red-text" color=red;>yaba daba dooo</h2>'


@app.get('/calc/<year>')
def calc_age(year):
    year = int(year)
    return f' your age {2025 - year}'


@app.get('/len/<name>')
def name_len(name):
    return f'{name} contains {len(name)} letters '


@app.get('/formula/<a>/<b>')
def sum_them(a, b):
    a = int(a)
    b = int(b)
    return f' {a} + {b} = {a + b}'


if __name__ == '__main__':
    app.run(port=5050)

# 1 - # write or add  a flask application
# that gets the user name from the
# client and print how many letters in his name
# the url is  /len/<name>

# 2 get from the user formula and return the answer for it  (sum)

# the url is  /formula/<a>/<b>
# returns a+b in a str

# http://localhost:<port>/resource
