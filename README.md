# learning_flask_BE223A

# Programming Lab 223A tutorial

# Building an online poll and displaying its results with Flask

## Tutorial Outline

### Install

#### Installing anconda, virtual env, flask

- First install anconda
- Install the virtual environement python module
```bash
 conda install -c anaconda virtualenv
 ```
 - Navigate to the directory where you will create your Flask app.
 ```bash
 mkdir folder_name
 cd folder_name
 ```
 - Type:
 ```bash
 virtualvenv venv
 ```
 - Activate virtual environment
 ```bash
  source activate venv
  ```
  - Install flask in venv
  ```bash
  pip install Flask
  ```

#### Create the following file structure inside folder_name

- create main.py file 
```bash
touch main.py
```
- create a directory for the static files
```bash
mkdir static
```
- create directories inside static for images, css and js files.
```bash
mkdir img
mkdir css
mkdir js
```
- create a direcory for templates
```bash
mkdir templates
```

### Hello World app

- create Hello world view
- Introduction to the Request-Response cycle

### User view

### Templates

### Bootstrap

- install bootstrap
```bash
pip install flask-bootstrap
```

### Using a base template

### Extending Navigation Bar

### Adding static files

- Adding header icons

### Web forms

### Creating a poll

### Creating a thank you template

### Storing poll's data

### Poll's data visualization

### Data Analysis module

### Displaying Results

### Displaying Results using bar charts

### Rendering Markdown

# Aknowledgements

- [Miguel Grinebrg-Flask Web DEvelopment Book](https://coddyschool.com/upload/Flask_Web_Development_Developing.pdf)
- [Lalith Polepeddi](https://www.lynda.com/Flask-tutorials/course-overview/521231/529872-4.html?srchtrk=index%3a1%0alinktypeid%3a2%0aq%3aflask%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2)
- [Gabor Szabo](https://code-maven.com/a-polling-station-with-flask)
- [Hans Petter Langtangen and Anders E. Johansen](http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_flask013.html)
