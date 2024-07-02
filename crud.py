from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)

    return {'books': output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)

    return {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

# This class defines a model for a Book object with attributes
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))


    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"