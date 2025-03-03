class Post:
    def __init__(self, id, title, author, content, date_posted):
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.date_posted = date_posted

    def __str__(self):
        return f' Post <{self.title} {self.author} {self.content} {self.date_posted}>'


# p1 = Post(1, 'greet', 'hodi', 'hello from the other side ', '11/12')
# print(p1.__dict__)