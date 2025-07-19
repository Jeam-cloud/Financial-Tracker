# Financial-Tracker

A full-stack personal finance tracker designed to help users securely manage and visualize their spending. The app allows uploading of RBC bank statement CSV files, user-specific data storage with authentication, and generates monthly spending summaries for better financial management.

https://github.com/user-attachments/assets/752be2fb-503c-48f9-8317-386a91d66d13

## Features
- **User Authentication**: Secure login and signup using Flask-Login, ensuring each user's data is private and separated.

- **Persistent SQLite Database**: Stores users and their uploaded transactions using SQLAlchemy with SQLite as the database engine.

- **CSV Upload**: Upload RBC bank statement CSVs to populate personal transaction tables.

- **Transaction Table**: Clean and responsive table displaying transaction history.

- **Monthly Summaries**: Automatic calculation of monthly spending totals.

- **Flask Backend**: Handles file processing, routing, authentication, and session management.

- **HTML/CSS/JavaScript Frontend:** Simple, responsive UI using vanilla JS with fetch API for backend communication.

- **sortable table**: users are able to sort the table to display only specific data they prefer

## Tech Stack
Python

Flask

SQLite (via SQLAlchemy ORM)

Flask-Login

Flask-WTF

pandas

HTML / CSS / JavaScript (Vanilla)

## Prerequisites
`pip install -r requirements.txt`
Or manually:

`pip install flask Flask-SQLAlchemy flask-login flask-wtf pandas`

## Running the App

`python finance.py`


## Future Improvements
- Graphs using Chart.js for interactive browser-based charts.

- Multi-bank CSV support.

- Category-based analytics and auto-categorization.

- Improved dashboard UI.

Thank you for reading!
