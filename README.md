# resource-package

## Table of Contents
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
