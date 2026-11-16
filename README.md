# Analyst Support Tool

This is a small web application I made with Python and Flask. It lets you search for people and organisations, add new information and see how different records are connected.

I wanted to build something practical where I could work with a database and learn more about how the different parts of a web application fit together.

## Features

- Search for people by name.
- Search for organisations by name or country.
- View organisations connected to a person.
- View people connected to an organisation.
- Add new people with notes.
- Add new organisations with country information.
- Log searches and changes to keep track of activity.

## Technologies

- **Python** – application logic
- **Flask** – web framework
- **SQLite** – database
- **HTML and CSS** – user interface
- **Jinja2** – displaying dynamic content

## Project structure

```text
analytikerstod/
│
├── app.py
├── models.py
├── service.py
├── import_people.py
├── people.csv
├── requirements.txt
├── README.md
│
└── templates/
    └── search.html
```

## How it works

The application is divided into a few different parts:

- `app.py` handles the Flask routes and user requests.
- `service.py` handles the search logic and brings together information from the database.
- `models.py` contains the database functions, including queries and operations for people, organisations and logs.
- `search.html` displays the forms and search results.

The database uses relationships between people and organisations, which makes it possible to find related information in both directions.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/linasidani/analytikerstod.git
cd analytikerstod
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the environment

On macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
python -m flask --app app run --debug
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Test data

The project includes a CSV file with fictional people that can be imported using:

```bash
python import_people.py
```

The import script checks whether a person already exists before adding them, which helps avoid duplicate entries.

## Current status

The main features are working, including searching, adding people and organisations, and viewing their connections.

I built the project to get more practical experience with Python, Flask and SQLite. There are still things I want to add and improve, especially in the interface, but I'm happy with how the project is coming together.
