A small project working on the skill to upload an image and store it in a database. 

## Installation instructions

These instructions are for macOS, and it is assumed that that the following are already installed:

* pipenv
* python 
* PostgreSQL 

After cloning the repository, using the CLI, change into the top-level directory of the locally cloned version. Then execute the following commands in sequence:

**Install any dependencies and set up your virtual environment**
* pipenv install 

**Activate your virtual environment**
* pipenv shell

**Create a development database**
* createdb uploads

**Seed your databases**
* psql uploads < seeds/upload.sql

**Run the app**
; python app.py

At this stage, the back-end server should be running. Open the following url in your browser: 

http://localhost:5001
