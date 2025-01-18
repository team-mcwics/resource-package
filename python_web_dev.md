# Crash course: web development with Python (+ other project ideas)

_Created for Hack McWiCS '25_

We will use Flask in this tutorial. Flask is a simple web framework for Python. It helps you build web applications quickly by providing the basic tools you need, like handling web requests and routing URLs. This way, you won't have to write a lot of the methods yourself. You can also easily connect it to a database to store information.

## Table of contents

1. [Other related project ideas](#other-related-project-ideas)
2. [Prerequisites](#prerequisites)
3. [A brief primer on Python projects](#projects-in-python)
4. [Setting up a virtual environment (highly recommended)](#setting-up-a-virtual-environment)
5. [Web servers](#web-servers)
6. [Setting up a basic Flask server](#setting-up-a-basic-flask-server)
7. [What now?](#what-now)
8. [Setting up a database with Flask](#setting-up-a-database-with-flask)
9. [More tutorials on Flask](#more-tutorials-on-flask)

---

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## Other related project ideas

Django is a bit more complicated, but has more features than Flask. Check out the official Django site: [https://www.djangoproject.com/start](https://www.djangoproject.com/start)

If you're purely interested in building an API, check out FastAPI: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)

Use ExpressJS (a JavaScript web framework) to build a JavaScript-based web application: [https://expressjs.com](https://expressjs.com)

Build a Chrome extension (it's good fun, and you only need to know JavaScript, HTML, CSS): [https://developer.chrome.com/docs/extensions/get-started](https://developer.chrome.com/docs/extensions/get-started)

Learn React, a very popular library for frontend development: [https://react.dev/learn](https://react.dev/learn)

Quickly build a React-based web application using NextJS: [https://nextjs.org](https://nextjs.org)

Use OpenCV to capture video input from your webcam and create a script to do something with it: [https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera](https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera)

Call a Web API (or multiple): [https://apilist.fun](https://apilist.fun)

Scrape websites with Selenium and Beautiful Soup: [https://www.codecademy.com/article/web-scrape-with-selenium-and-beautiful-soup](https://www.codecademy.com/article/web-scrape-with-selenium-and-beautiful-soup)

Build a Discord bot with Python, or even serve both a Discord bot and another application with your own API: [https://discordpy.readthedocs.io/en/stable](https://discordpy.readthedocs.io/en/stable)

Use React Native with Expo to build a mobile app: [https://reactnative.dev/docs/environment-setup](https://reactnative.dev/docs/environment-setup)

Render 3D scenes with the JavaScript engine (making it possible for them to be displayed in your browser): [https://threejs.org](https://threejs.org)

Create an application with live updates (ex. for a multiplayer game or chatting) with Socket.IO: [https://socket.io/get-started/chat](https://socket.io/get-started/chat)

...or using with Google Firebase: [https://deadsimplechat.com/blog/firebase-chat-app-tutorial](https://deadsimplechat.com/blog/firebase-chat-app-tutorial)

You can even use SocketIO with Flask: [https://flask-socketio.readthedocs.io/en/latest/getting_started.html](https://flask-socketio.readthedocs.io/en/latest/getting_started.html)

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## Prerequisites

1. Make sure you have Python installed. If you don't, you will need to download it here: [https://www.python.org/](https://www.python.org/)

To check if it installed correctly, open your command line terminal and type:

```bash
python --version
```

This should print:

```bash
Python 3.x.x
```

with your current version of Python.

2. Install pip, the Python package installer, if it is not already installed. You can check if pip is installed by running `pip --version` in your command line.
3. Make sure you have an IDE installed, for example, VSCode: [https://code.visualstudio.com/](https://code.visualstudio.com/).

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## Projects in Python

### Executing a Python file

Python files are indicated by the `.py` file extension. To run a Python file from the command line, you simply type:

```bash
python filename.py
```

When you create a project, it's best practice to separate your code into multiple Python files. For example, you could have one module storing code for one class, and then import it as needed.

Create a module like so:

```python
# dog.py
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_human_years(self):
        return self.age * 7

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"
```

...and import it like this:

```python
# main.py
from dog import Dog

my_dog = Dog(name="Buddy", age=5)
print(my_dog) # This prints "Dog(name=Buddy, age=5)"
```

### The main namespace

You can read more about namespaces here: [https://www.geeksforgeeks.org/namespaces-and-scope-in-python/](https://www.geeksforgeeks.org/namespaces-and-scope-in-python/).

The `__main__` namespace is created when the Python interpreter runs a script or module. Any code inside of `if __name__ == "__main__"` will only execute if the script is run directly. For example:

```python
def test_method():
    print("I only want to print this if I'm testing!")

def main():
    print("This script is being run directly.")

print("This will print if I run this module from another Python file.")

if __name__ == "__main__":
    main()
    test_method()
```

You might do this if you _don't_ want to run certain methods, for example while testing or debugging. If you place these methods inside of the `if __name__ == "main__"` block, they'll only be run if you execute the module file directly.

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## Setting up a virtual environment

A virtual environment is a tool that helps to keep dependencies required by different projects in separate places, by creating isolated Python environments for them. This is especially useful when you have multiple projects with different dependencies.

If you're collaborating, you might want to use a `requirements.txt` file to keep track of your dependencies. You should also separate your development dependencies (tools you use to make developing easier, but that aren't required for the app to run) in a `dev-requirements.txt` file. That way, it's easy for your teammates to download whatever dependencies you add without cursing you forever.

For example:

```
# requirements.txt
flask==2.3.0
sqlalchemy==2.0.0

# dev-requirements.txt
pytest==7.4.0
flake8==6.1.0
```

Then, to install dependencies, you just need to run:

```
pip install -r dev-requirements.txt
```

1. **Install `virtualenv`**

First, you need to install `virtualenv` if you haven't already. You can do this using `pip`:

```bash
pip install virtualenv
```

2. **Create a virtual environment**

Navigate to your project directory and create a virtual environment by running:

```bash
virtualenv venv
```

Here, `venv` is the name of your virtual environment folder. You can name it anything you like.

3. **Activate the virtual environment**

To start using the virtual environment, you need to activate it. The command to activate the virtual environment depends on your operating system:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

After activation, your command line prompt will change to indicate that you are now working inside the virtual environment.

4. **Install dependencies**

With the virtual environment activated, you can now install the dependencies for your project. These can be done with the `pip` package manager.

5. **Deactivate the virtual environment**

When you are done working on your project, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to the global Python environment.

By using a virtual environment, you can ensure that your project dependencies are isolated and do not interfere with other projects on your system.

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## Web servers

A web server is a software application that handles requests from clients (such as web browsers) and serves them web pages or other content. When you type a URL into your browser and hit enter, your browser sends a request to a web server, which then processes the request and sends back some content.

### Running a web server locally

The Mozilla web documentation is a great source for learning more about how the web works: [https://developer.mozilla.org/en-US/](https://developer.mozilla.org/en-US/)

When you run a web server locally, it means you are running the server on your own computer instead of on a remote server. This is often done during development so you can test your web application before deploying it to a live server.

### Ports

A port is a communication endpoint that allows your computer to differentiate between different types of network traffic. When you run a web server, it listens for incoming requests on a specific port number.

For example, when you run a Flask server locally, it typically listens on `port 5000` by default. This means you can access your web application by navigating to [http://localhost:5000](http://localhost:5000) in your web browser. The localhost part refers to your own computer, and 5000 is the port number.

Different applications and services use different ports to communicate. For instance, web servers commonly use port 80 for HTTP traffic and port 443 for HTTPS traffic.

### Requests

When you interact with a web server, you are sending requests and receiving responses. A request is a message sent by a client (such as a web browser) to a server, asking for some action to be performed. There are several types of requests, but the most common ones are:

1. **GET**: Requests data from a specified resource. For example, when you visit a webpage, your browser sends a GET request to the server to fetch the page content.
2. **POST**: Submits data to be processed to a specified resource. For example, when you fill out a form on a website and click submit, your browser sends a POST request with the form data.
3. **PUT**: Updates a current resource with new data.
4. **DELETE**: Deletes a specified resource.

Each request consists of:

- **URL**: The address of the resource you want to access.
- **Method**: The type of request (GET, POST, etc.).
- **Headers**: Additional information sent with the request, such as authentication tokens.
- **Body**: Data sent with the request (mainly used with POST and PUT requests).

When the server receives a request, it processes it and sends back a response, which includes:

- **Status Code**: Indicates the result of the request (e.g., 200 for success, 404 for not found).
- **Headers**: Additional information about the response.
- **Body**: The content of the response (e.g., HTML, JSON).

In the next sections, you will set up a Flask application that will be able to receive requests and send responses back.

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## Setting up a basic Flask server

To set up a Flask server, you need to install Flask first. Make sure that you're inside of the right folder. Open your command line, and type the following command.

```bash
pip install Flask
```

Next, create a new Python file (e.g., `app.py`) and add the following code to set up a basic Flask server:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Creating routes

In Flask, you can create routes using the `@app.route` decorator. Each route corresponds to a URL that the server can respond to.

By passing `__name__` to the Flask constructor, you allow Flask to determine the root path of your application, which is useful for locating resources like templates and static files.

Here is an example of how to create multiple routes:

```python
from flask import Flask  # Import the Flask class

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/')  # Define the route for the home page
def home():
    return "Hello, Flask!"  # Return a response for the home page

@app.route('/about')  # Define the route for the about page
def about():
    return "This is the about page."  # Return a response for the about page

if __name__ == '__main__':  # Check if the script is run directly
    app.run(debug=True)  # Run the Flask application in debug mode
```

### Running the server

To run the Flask server, simply execute the Python file:

```bash
python app.py
```

You should see output indicating that the server is running, and you can visit `http://127.0.0.1:5000/` in your web browser to see the result.

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

Now you have a basic Flask server up and running with multiple routes. If you want to see your `about` route, you can go to `http://127.0.0.1:5000/about`.

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## What now?

### Serving HTML pages

You can use Flask to serve templated webpages, which can be rendered with or without data from your server. Flask is limited in building full-stack web applications compared to say, ExpressJS, but it can be done. Here's a small example using basic HTML:

1. **Create a templates folder**
   Create a folder named `templates` in the same directory as your `app.py` file. Inside the `templates` folder, create an HTML file named `index.html`:

   ```html
   <!-- templates/index.html -->
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Home</title>
     </head>
     <body>
       <h1>{{ title }}</h1>
       <p>{{ message }}</p>
     </body>
   </html>
   ```

2. **Update your Flask app**
   Modify your `app.py` file to render the HTML template:

   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html', title='Hello, Flask!', message='Welcome to Flask!')

   if __name__ == '__main__':
       app.run(debug=True)
   ```

Now, when you run your Flask server and visit `http://127.0.0.1:5000/`, you should see the rendered HTML page with the title and message.

### Using Flask as an API

To use Flask as an API backend, you can set up routes that return JSON data. This is useful when you want to interact with your backend using HTTP requests. When the client (for example, another application) requests something, you can send data back.

A brief example:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "This is some data from the API"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```

To test your API, run your application. Then, visit `http://127.0.0.1:5000/api/data` in your browser or using a tool like Postman to see the JSON response:

```
{
  "message": "This is some data from the API"
}
```

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## Setting up a database with Flask

Databases can be useful for persisting data across refreshes. A relational database can be thought of as like your typical spreadsheet: each row contains properties about your data. We often use SQL (a language) to communicate with relational databases. A nice thing about relational databases is that you can connect multiple tables together. For example, you could use connect your table storing user information to a table storing car information by attaching a user ID to each car.

There are many relational database management systems. In this tutorial, we use SQLite, but PostgreSQL is also a popular option. You can also use a non-relational database such as MongoDB, which stores data as JSON-like documents.

We can also use object-relational mapper (ORM) tools to make formatting our data a bit easier. We define what are known as schemas as a template for what our data should look like. Here, we use SQLAlchemy.

1. **Install Flask-SQLAlchemy**
   Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy, a SQL toolkit for Python. Install it using pip:

   ```bash
   pip install Flask-SQLAlchemy
   ```

2. **Configure the database**
   In your Flask application, configure the database URI. Add the following code to your `app.py`:

   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
   db = SQLAlchemy(app)
   ```

   This example uses SQLite, a lightweight database. The database file will be named `site.db`.

3. **Create a database model**
   Define a model for your database. Add the following code to `app.py`:

   ```python
   class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
             return f"User('{self.username}', '{self.email}')"
   ```

   This creates a `User` table with `id`, `username`, and `email` columns.

4. **Create the database**
   Open a Python shell and run the following commands to create the database and tables:

   ```python
   from app import db
   db.create_all()
   ```

5. **Add data to the database**
   You can add data to the database using the following code:

   ```python
   from app import db, User

   user_1 = User(username='JohnDoe', email='john@example.com')
   db.session.add(user_1)
   db.session.commit()
   ```

6. **Query the database**
   Retrieve data from the database using queries:

   ```python
   users = User.query.all()
   print(users)
   ```

Now you have a basic database set up with Flask and SQLAlchemy. You can expand this by adding more models and queries as needed.

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## More tutorials on Flask

DigitalOcean Flask and PostgreSQL tutorial: [https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application)

Jinja templating engine and Flask tutorial: [https://codingnomads.com/python-flask-jinja-template-jinja2](https://codingnomads.com/python-flask-jinja-template-jinja2)

SQLAlchemy and Flask: [https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)
