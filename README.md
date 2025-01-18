# Hack McWiCS 2025: Resource Package Guide 💻

Welcome to the **Hack McWiCS 2025 Resource Package**! This guide is crafted to help you hit the ground running with your hackathon project. Whether this is your first hackathon or you're looking on exploring new technologies, you'll find a variety of tools, tutorials, and best practices to support you.

If you’re stuck on anything, don’t be scared to ask for help from our mentors. They’re here to support you all throughout the weekend!! There are no dumb questions (like actually)!

Check the **Table of Contents** for a comprehensive overview of the topics covered!

# Table of Contents
- [Figma & UI/UX Design](#figma--uiux-design)
    - [UI/UX Design]([#uiux-design)
    - [Figma](#figma)
        - [Getting started with Figma](#getting-started-with-figma)
- [HTML/CSS](#htmlcss)
    - [What is HTML?](#what-is-html)
    - [What is CSS?](#what-is-css)
    - [Getting started with HTML/CSS](#getting-started-with-htmlcss)
- [React](#react)
    - [How React Works](#how-react-works)
    - [Getting started with React](#getting-started-with-react)
- [Angular](#angular)
    - [How Angular Works](#how-angular-works)
    - [Getting started with Angular](#getting-started-with-angular) 
- [GameDev with PyGame](#gamedev-with-pygame)
    - [What is PyGame](#what-is-pygame)
    - [Creating your First PyGame Project](#creating-your-first-pygame-project)
- [Databases with Java Spring Boot & PostgreSQL](#databases-with-java-spring-boot--postgresql)
    - [What is a Database? Spring Boot? PostgreSQL?](#what-is-a-database-java-spring-boot-postgresql)
    - [Creating your First Java Spring Boot & PostgreSQL project](#creating-your-first-java-spring-boot--postgresql-project)
- [Using APIs with .NET](APIs%20%26%20dotnet/README-APIs%26dotnet.md)
- [Working with Data/ML on Pandas and HuggingFace](#working-with-data-and-machine-learning-on-pandas-and-huggingface)
- [Web dev with Python](#web-dev-with-python-and-project-ideas)
    - [Other related project ideas](#other-related-project-ideas)
    - [Prerequisites](#prerequisites)
    - [A brief primer on Python projects](#projects-in-python)
    - [Setting up a virtual environment (highly recommended)](#setting-up-a-virtual-environment)
    - [Web servers](#web-servers)
    - [Setting up a basic Flask server](#setting-up-a-basic-flask-server)
    - [What now?](#what-now)
    - [Setting up a database with Flask](#setting-up-a-database-with-flask)
    - [More tutorials on Flask](#more-tutorials-on-flask)
- [Devpost](#devpost)
    - [How to Submit a Project](#how-to-submit-a-project)
    - [What to Include in Your Submission](#what-to-include-in-your-devpost-submission)
    - [How to View Previous Projects](#how-to-view-previous-projects)    


# Figma & UI/UX Design

## UI/UX Design
User Interface (UI) Design focuses on the look and feel of a product. User Experience (UX) Design, on the other hand, is about how a user interacts with the product. A combination of these two features can lead to a product that is both aesthetically pleasing and easy to use. 

### Important Concepts of UI/UX Design
- **User-Centered Design**: Always design with the user's needs in mind
- **Consistency**: Keep elements (buttons, colors, fonts, etc.) consistent throughout the design
- **Accessibility**: Ensure your designs are usable by as many people as possible, including those with disabilities
- **Visual Hierarchy**: Arrange elements to guide the user's attention effectively (Ex: you can draw more attention to a specific button by making its color stand out from the rest of the page)

### Resources
- [UI/UX Learning Guide](https://github.com/hendurhance/ui-ux)


## Figma 
Figma is one of the most popular tools for UI/UX design. It's a free web-based platform for designing wireframes and prototypes for your project. To create a project that looks professional and communicates your ideas effectively, Figma provides a simple, beginner-friendly interface where you can experiment with layouts, colors, and interactions.

### Getting started with Figma
- Check out this YouTube playlist made my Figma: [Figma for Beginners](https://help.figma.com/hc/en-us/sections/4405269443991-Figma-for-beginners-4-parts)
- Figma also offers a lot of free templates: [Figma Templates](https://www.figma.com/templates/)

<br>

# HTML/CSS
HTML and CSS are the building blocks of the web and will help you create functional websites from scratch.

### What is HTML?
HTML (HyperText Markup Language) is the structure of a webpage. Think of it as the foundation of a building—it holds everything together and defines what appears on the page. 

With HTML, you can:
* Add headings, paragraphs, and lists
* Insert images and links
* Create tables and forms for user interaction

For example:
```html
<html>
<head>
    <title>My First Webpage</title>
</head>
<body>
    <h1>Welcome to My Website!</h1>
    <p>This is a paragraph of text about my website.</p>
    <a href="https://www.example.com">Visit Example</a>
</body>
</html>
```

### What is CSS?
CSS (Cascading Style Sheets) is what makes your webpage look good. It's like the paint and decoration of you building. CSS is used to style HTML elements by changing their colors, sizes, layouts, and more.

With CSS, you can:
* Change text colors, fonts, and sizes
* Add spacing between elements
* Arrange elements in flexible layouts like grids or columns

For example:
```css
h1 {
    color: blue;
    font-family: Arial, sans-serif;
    text-align: center;
}

/* Style the paragraph */
p {
    font-size: 16px;
    line-height: 1.5;
    color: gray;
}
```

### Getting started with HTML/CSS
1. Make sure you have a text editor like VS Code
2. Begin by creating a simple HTML file and adding a heading, some text, etc.
3. Gradually add CSS to style these elements and experiment with different colors, fonts, and layouts

### Resources
- W3Schools is a very popular resource for learning code: [w3schools](https://www.w3schools.com/)
- freeCodeCamp is also a very useful web development bootcamp: [freeCodeCamp](https://www.freecodecamp.org/)
- Don't forget that most students can gain free access to Udemy courses through their university! Udemy has thousands of courses on all different areas of web development.

<br>

# React
React is a popular JavaScript library for building user interfaces. It's widely used for developing web applications that are fast, interactive, and scalable. 

Here are some reasons why you should learn React:
- **Reusable Components**: Write a burtton or a card layout once, and resuse it throughout your app
- **Interactive UI**: React makes it easy to create apps that respond to user interactions without needing to reload the page
- **State Management**: Keep track of data (like user input or API responses) and update the UI automatically when something changes
- **Community**: React has countless libraries and tools to simplify development

### How React Works
React uses a component-based architecture, meaning your app is built with independent pieces called components. Components are like building blocks that you can customize and combine to create complex interfaces. 
- JSX: React uses a synteax called JSX (JavaScript XML), which lets you write HTML-like code inside JavaScript
    Ex: ```const element = <h1>Welcome to React!</h1>; ```
- State and Props:
    - **State** is data that belongs to a component and can change over time
    - **Props** are inputs you pass to a components to make it dynamic and reusable

### Getting started with React
- Code Editor: VS Code is highly recommended [VS Code](https://code.visualstudio.com/)
- Node.js: React apps use Node.js for running JavaScript outside the browser and managing dependencies [Node.js](https://nodejs.org/en)

**Setting up your first React app**
1. **Use Create React App**: run this in your terminal
   ```bash
   npx create-react-app my-first-app
    cd my-first-app
    npm start
   ```
   This will set up a basic React app and open it in your browser
2. **Understand the File Structure**:
   - **src**: this folder contains the main files where you'll write your components
   - **App.js**: the starting point of your React app
   - **index.js**: the file that connects React to the DOM (Document Object Model)

Here's a basic example of a React component that displays a greeting: 
```javascript
import React from 'react';

function App() {
    return (
        <div>
            <h1>Hello, React!</h1>
            <p>This is my first React app.</p>
        </div>
    );
}

export default App;
```

Once you've got the basics down, try making simple projects like:
- A to-do list
- A weather app using an API
- A personal portfolio site

### Resources
- [React Tutorial for Beginners](https://www.youtube.com/watch?v=SqcY0GlETPk&ab_channel=ProgrammingwithMosh)
- [React Official Docs](https://react.dev/)
- [freeCodeCamp](https://www.freecodecamp.org/)
- [Codecademy](https://www.codecademy.com/)

<br>

# Angular
Angular is another powerful framework for building web applications. It is a TypeScript-based framework designed to make building web applications easier and more organized. Unlike libraries like React, which focus mainly on the view layer, Angular is a full-fledged framework—it gives you everything you need for your app in one package, from routing to state management.

### How Angular Works
1. **Modules**: Angular apps are organized into modules. Every app has a root module (AppModule), and you can create feature modules for better organization
2. **Components**: Each UI part of you app is a component. Components consist of HTML, CSS, and TypeScript which adds logic
3. **Data Binding**
    - **Interpolation**: Display dynamic values in the template
      ```<p>{{ message }}</p>```
    - **Event Binding**: Respond to user actions
      ```<button (click)="sayHello()">Click Me</button>```

### Getting started with Angular
- Node.js: For running Angular commands and managing dependencies [Node.js](https://nodejs.org/en)
- Angular CLI (Command Line Interface): Makes setting up and managing Angular projects easier
    - To install Angular CLI, run:
      ```npm install -g @angular/cli```

**Setting up your first Angular app**
1. Create a new Angular project by running the following command in your terminal
   ```
   ng new my-first-angular-app
    cd my-first-angular-app
    ng serve
   ```
   This will create a new Angular project and start a development server.
   Open your browser and go to http://localhost:4200 to see your app in action.
2. Understand the folder structure
   - **src/app**: where your components and logic live
   - **app.modeul.ts**: the main component that controls your app's view
   - **app.module.ts**: the file where your app's components and services are registered

**Beginner Project Ideas**
- A personal blog with multiple pages
- A to-do list app with add/delete functionality
- A simple weather app using an API

### Resources
- [Angular Docs](https://angular.dev/)
- [freeCodeCamp](https://www.freecodecamp.org/)
- [Net Ninja's Angular Tutorials](https://www.youtube.com/c/TheNetNinja)
- [Academind's Angular Course on YouTube](https://www.youtube.com/@Academind)

<br>

# GameDev with PyGame

### What is PyGame
GameDev (also known as Game Development) is the process of creating video games, which involves design, programming, art, audio, and more. 

PyGame is a game development library. It's a set of Python modules designed for writing video games. PyGame is ideal for beginners in programming and game development as it's user-friendly and built on python. In fact, Python's syntax is straightforward, making it easier to understand and use. PyGame is great as it provides functionalities like creating windows, drawing shapes, and managing user input, simplifying the game development process. It supports 2D graphics and allows for easy loading and rendering of images. It also handles sound effects and music, enabling the creation of fully-featured games. PyGame also includes an efficient event handling system. It can detect keyboard and mouse events, which are crucial for interactive gameplay. 

## Creating your First PyGame Project
Learn how to create a 2D game called **Space Protector** [here](GameDev%20&%20PyGame/README-GameDev&PyGame.md#readme-pygame-basics-and-space-protector-overview). The game involves players controlling a spaceship to defend themselves from incoming asteroids while earning points by destroying them.
<br>

# Databases with Java Spring Boot & PostgreSQL

## What is a Database? Java Spring Boot? PostgreSQL?
A **database** is an organized collection of data that can be easily accessed, managed, and updated. Think of it as a virtual filing system where your application stores information, such as user details or product listings. 

**Spring Boot** is a Java framework that simplifies building web applications and APIs by automating configuration and reducing boilerplate code. It’s beginner-friendly, provides built-in tools for common tasks (like connecting to databases), and lets you focus on creating features instead of setup.

**PostgreSQL** is a powerful, open-source relational database system. It’s beginner-friendly and supports SQL (Structured Query Language) for querying and managing data.

## Creating your First Java Spring Boot & PostgreSQL project
Let's try creating a simple web application where users can add, view, and delete items from a database.

### **Tech Stack:**
- **Backend:** Java Spring Boot
- **Database:** PostgreSQL
- **Tools:** IntelliJ IDEA (or your favorite IDE), Postman for API testing

### Step 1: Set Up Your Environment

1. **Install JDK:**
   - Download and install Java Development Kit (JDK) from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or [OpenJDK](https://openjdk.org/).

2. **Install PostgreSQL:**
   - Download and install PostgreSQL from [postgresql.org](https://www.postgresql.org/).
   - During installation, set a password for the `postgres` user and note it down.

3. **Install Spring Boot Tools:**
   - Use an IDE like IntelliJ IDEA or Eclipse.
   - Install Maven (if not bundled with your IDE).

4. **Postman (Optional):**
   - Download Postman for testing your API: [Postman](https://www.postman.com/downloads/).

### Step 2: Create a Spring Boot Project

1. **Generate a Spring Boot Project:**
   - Go to [Spring Initializr](https://start.spring.io/).
   - Choose the following options:
     - Project: **Maven**
     - Language: **Java**
     - Dependencies:
       - Spring Web
       - Spring Data JPA
       - PostgreSQL Driver
   - Click **Generate** and download the project.

2. **Import the Project:**
   - Open your IDE and import the project as a Maven project.

### Step 3: Configure PostgreSQL

1. **Create a Database:**
   - Open the PostgreSQL command-line interface (psql) or a GUI tool like pgAdmin.
   - Create a new database:
     ```sql
     CREATE DATABASE hackathon_db;
     ```

2. **Configure `application.properties`:**
   In `src/main/resources/application.properties`, add your database configuration:
   ```properties
   spring.datasource.url=jdbc:postgresql://localhost:5432/hackathon_db
   spring.datasource.username=postgres
   spring.datasource.password=your_password

   spring.jpa.hibernate.ddl-auto=update
   spring.jpa.show-sql=true
   spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
   ```

### Step 4: Build Your First API Following Spring Boot Architecture
Spring Boot follows a layered architecture to separate concerns and organize code effectively. Each layer has a distinct purpose and works together to deliver functionality.

1. **Model Layer (Data Layer)**
This layer defines the structure of your data and maps it to the database.

**Purpose:** Represents the database table as a Java object. Each instance corresponds to a row in the database.

**Example:**
```java
package com.example.demo.model;

import jakarta.persistence.*;

@Entity
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    public Item() {}

    public Item(String name) {
        this.name = name;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

2. **Repository Layer (Data Access Layer)**
This layer interacts directly with the database to perform CRUD operations.

**Purpose:** Provides an abstraction over database queries, making data access easier. 

**Connection:** Called by the Service Layer to fetch or save data. 

**Example:**
```java
package com.example.demo.repository;

import com.example.demo.model.Item;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ItemRepository extends JpaRepository<Item, Long> {}
```

3. **Service Layer (Business Logic Layer)**
This layer contains the application’s core logic and connects the Controller with the Repository.

**Purpose:** Processes data from the repository before passing it to the controller or vice versa. 

**Connection:** Acts as an intermediary between the Controller and Repository layers. 

**Example:**
```java
package com.example.demo.service;

import com.example.demo.model.Item;
import com.example.demo.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ItemService {

    @Autowired
    private ItemRepository itemRepository;

    public List<Item> getAllItems() {
        return itemRepository.findAll();
    }

    public Item createItem(Item item) {
        return itemRepository.save(item);
    }

    public void deleteItem(Long id) {
        itemRepository.deleteById(id);
    }
}
```

4. **Controller Layer (API Layer)**
This layer handles HTTP requests and sends responses back to the client.

**Purpose:** Exposes API endpoints for the client to interact with the application. 

**Connection:** Calls methods from the Service Layer to perform operations. 

**Example:**
```java
package com.example.demo.controller;

import com.example.demo.model.Item;
import com.example.demo.service.ItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/items")
public class ItemController {

    @Autowired
    private ItemService itemService;

    @GetMapping
    public List<Item> getAllItems() {
        return itemService.getAllItems();
    }

    @PostMapping
    public Item createItem(@RequestBody Item item) {
        return itemService.createItem(item);
    }

    @DeleteMapping("/{id}")
    public void deleteItem(@PathVariable Long id) {
        itemService.deleteItem(id);
    }
}
```

### **How the Layers Work Together**
1. The **client** sends an HTTP request (e.g., `GET /api/items`) (ex client: frontend).
2. The **Controller** handles the request and calls the **Service** to process it.
3. The **Service** interacts with the **Repository** to fetch or manipulate data.
4. The **Repository** queries the **database**, retrieves the result, and passes it back through the layers.
5. The **Controller** sends a response back to the client.


### Step 5: Test Your Application

1. **Run the Application:**
   - Run the `DemoApplication` class in your IDE.

2. **Test with Postman:**
   - **Get All Items:**
     - Method: `GET`
     - URL: `http://localhost:8080/api/items`
   - **Create an Item:**
     - Method: `POST`
     - URL: `http://localhost:8080/api/items`
     - Body (JSON):
       ```json
       {
           "name": "Hackathon Project"
       }
       ```
   - **Delete an Item:**
     - Method: `DELETE`
     - URL: `http://localhost:8080/api/items/1`

### Next Steps
- Add more features, such as user authentication or advanced queries.
- Create a frontend to interact with your API (e.g., React.js, Vue.js).
- Deploy your application using platforms like Heroku or AWS.

### **Resources**
- [Spring Boot Documentation](https://spring.io/guides)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Spring Boot Architecture](https://www.javatpoint.com/spring-boot-architecture)
- [Postman Testing](https://www.guru99.com/postman-tutorial.html)
- [Step by step guide](https://talesofdancingcurls.medium.com/spring-boot-with-postgresql-a-step-by-step-guide-c451848f0184)
- [Connect React Frontend to Spring Boot Backend](https://www.dhiwise.com/post/a-step-by-step-guide-to-implementing-react-spring-boot) 

<br>

# Working with Data and Machine Learning on Pandas and HuggingFace

## Working with Data

In our world today, we have an overflowing amount of data available. Analysis of such data can lead to useful insights and conclusions. Further, manipulating the data for a machine learning model (data preprocessing) is an important step. Some common tasks include: 

- Handling null values (missing data) 
- Removing outliers 
- Scaling 
- Encoding the data (handling categorical features) 

## What is Pandas

Pandas is a powerful Python library used for data manipulation and analysis. It’s essential for preparing and cleaning data, which is a crucial step in machine learning workflows. 

Pandas provides two main data structures:
- pandas.Series: A one-dimensional array, similar to a list.
- pandas.DataFrame: A two-dimensional table, similar to an Excel spreadsheet.

## Basic Operations on Pandas

### 1. Install Pandas
In your terminal (with a virtual environment activated if you prefer), use the following command to install panda: 

`pip install pandas`

### 2. Import Pandas

In your python file, use the following import statement to import pandas: 

`import pandas as pd`

### 3. Loading Data 

Pandas can load data from multiple file types: 

Loading CSV file: `df = pd.read_csv('data.csv')`

Loading Excel file: `df = pd.read_excel('data.xlsx')`

Loading JSON file: `df = pd.read_json('data.json')`

### 4. Exploring the Data

Once the data is loaded, it’s important to explore it to understand its structure and identify issues.

View the first few rows:

`print(df.head())`

Check the structure of the dataset:

`print(df.info())`

Summary statistics of numerical columns:

`print(df.describe())`

### 5. Handling Null Values

Missing data is a common issue.

To identify missing values:

`print(df.isnull().sum())`

There are two ways to deal with missing values: 

1. Fill them (usually if it is a quantitative variable)

`df['Column'] = df['Column'].fillna(df['Column'].mean())  # Replace with mean`
`df['Column'] = df['Column'].fillna(method='ffill')  # Forward fill`
`df['Column'] = df['Column'].fillna(method='bfill')  # Backward fill`

2. Drop them 

`df = df.dropna()  # Drop rows with missing values`

`df = df.dropna(axis=1)  # Drop columns with missing values`

### 6. Removing Outliers

It is important to remove outliers because outliers can skew your analysis. A common method in removing outliers is using the IQR (interquartile range) definition, which is a statistical definition of outliers. 

`Q1 = df['Column'].quantile(0.25)`

`Q3 = df['Column'].quantile(0.75)`

`IQR = Q3 - Q1`

`lower_bound = Q1 - 1.5 * IQR`

`upper_bound = Q3 + 1.5 * IQR`

`df = df[(df['Column'] >= lower_bound) & (df['Column'] <= upper_bound)]`

## Extra Steps for ML 

### 1. Scaling the data

Scaling ensures all numerical features have the same range, which is important for machine learning algorithms.

There are two methods that you can choose from: 

#### a) Standardization (z-score scaling) = Scales data values so that they have a mean of 0 and a standard deviation of 1. This technique is useful when the distribution of the data is known and normal.

`from sklearn.preprocessing import StandardScaler`

`scaler = StandardScaler()`

`df[['Column1', 'Column2']] = scaler.fit_transform(df[['Column1', 'Column2']])`

#### b) Normalization (min-max scaling) = Scales data values to a specific range, usually between 0 and 1. This technique is useful when the distribution of the data is unknown or non-normal.

`from sklearn.preprocessing import MinMaxScaler`

`scaler = MinMaxScaler()`

`df[['Column1', 'Column2']] = scaler.fit_transform(df[['Column1', 'Column2']])`


### 2. Encoding Categorical Features 

Machine learning models often require numerical inputs. Therefore, we need to convert categorical columns (ex. gender, hair color) to numeric. Here are two common methods:

Label Encoding: 

`df['Category'] = df['Category'].astype('category').cat.codes`

One-Hot Encoding:

`df = pd.get_dummies(df, columns=['Category'], drop_first=True)`

## Using HuggingFace Pretrained Models

HuggingFace provides a library of pretrained models for tasks like text classification, translation, and more. 

You can feed the data you have on your pandas dataframe into a HuggingFace model to produce outputs. 

The easiest way to do this is to use the pipeline wrapper. For instance, here’s an example of how to use a dataset with a HuggingFace model for text classification:

```
from transformers import pipeline

# Load pretrained pipeline for sentiment analysis
classifier = pipeline("sentiment-analysis")

# Example: Apply the model to a text column in the dataframe
texts = df['TextColumn'].tolist()  # Convert text column to a list
results = classifier(texts) # results will be a list of dictionaries with the category the text was classified as stored under the key 'label'

# Add the predictions back to the dataframe
predictions = [result['label'] for result in results]
df['Predictions'] = predictions

print(df.head())
```

You can find more information on the HuggingFace Website for Pipelines: https://huggingface.co/docs/transformers/en/main_classes/pipelines

HuggingFace also offers a lot of other functionalities:

- HuggingFace Datasets: Access thousands of ready-to-use datasets for tasks like text classification, summarization, and translation. Load datasets directly with datasets.load_dataset(). Use the many built-in functions for preprocessing. Take a look at: https://huggingface.co/docs/datasets/en/index

- Transformers Library (Pretrained Models): A Python library that provides the tools to load, use, fine-tune, and train transformer-based models. Load and use specific pretrained models from the Model Hub for tasks like sentiment analysis, question answering, text generation, and image classification. Take a look at: https://huggingface.co/docs/transformers/en/index 
    - This is one of the most popular uses for HuggingFace!

- Model Hub: Explore and download over 100,000 pretrained models for NLP, computer vision, and audio tasks. Fine-tune or deploy models with ease, often requiring just a single line of code to load them. Take a look at: https://huggingface.co/docs/hub/en/models-the-hub

If you don't know where to start, the pipelines tool is a great starting point!

<br>

# Wev dev with Python and project ideas

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

## More tutorials on Flask

DigitalOcean Flask and PostgreSQL tutorial: [https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application)

Jinja templating engine and Flask tutorial: [https://codingnomads.com/python-flask-jinja-template-jinja2](https://codingnomads.com/python-flask-jinja-template-jinja2)

SQLAlchemy and Flask: [https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)


# Devpost
Devpost is the go-to platform for hackers to showcase their projects, connect with fellow hackers, and participate in hackathons. 

### How to Submit a Project
During Hack McWiCS, Devpost is the platform where you'll need to submit your hackathon project in order to be eligible for judging and prizes. Here's how:
1. Create a [Devpost](https://devpost.com/) account (if you don't have one already).
2. [Register](https://help.devpost.com/article/119-registering-for-a-hackathon) for the Hack McWiCS 2025 hackathon [here](https://hack-mcwics-2025.devpost.com/).
3. [Create](https://help.devpost.com/article/122-how-to-enter-a-submission) a submission (check note below).
4. [Submit](https://help.devpost.com/article/126-know-your-submission-steps) a project.
5. You can [edit](https://help.devpost.com/article/123-how-to-edit-a-submission) a submission any time before the deadline.

More information [here](https://help.devpost.com/category/20-submitting-to-a-hackathon)

> [!NOTE]  
> When first creating a project, only 1 team member needs to create a project and then that team member can invite all the other teammates to collaborate on the same project through the "Manage Team" tab. Each team member needs to create their own devpost account (step 1) and register for the Hack McWiCS 2025 hackathon devpost (step 2).

### What to Include in your Devpost Submission

Make sure to include the following in your Devpost submission:

- **What your project does** – Briefly describe the purpose and functionality of your project.
- **How you built your project** – Explain the technologies, tools, and frameworks you used, along with a high-level overview of the architecture and design.
- **Link to your project** – Provide a link to the project repository, live demo, or relevant materials.
- **Screenshots or a video of your project** – Include visuals to showcase the project in action, making it easier for others to understand what it looks like and how it works.

### How to View Previous Projects
You can also use Devpost to get inspiration for your next hack by exploring all of the projects submitted in previous editions of Hack McWiCS through the [project gallary](https://help.devpost.com/article/80-what-is-the-project-gallery).
- [Hack McWiCS 2024](https://hack-mcwics-2024.devpost.com/)
- [Hack McWiCS 2023](https://hack-mcwics-2023.devpost.com/)

