# Flask HTML Web & Database Project Starter

This is a starter project for you to use to start your Flask HTML web & database
projects.

It contains quite a lot of example code. You can use this to see how the various
parts of the project work, or you can delete it and start from scratch.

<!-- OMITTED -->


## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/web-applications-in-python-project-starter.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/web-applications-in-python-project-starter.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py
```

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```

## Running the tests

```shell
# To run the tests you will need two terminals, one to run the test server
# and one to run the tests. The test server must be running for the tests
# to work.

# In one terminal:
; ./run_test_server.sh

# In another terminal
; pipenv run pytest
```

## Running the dev server

Make sure you've stopped running the test server, and then:

```shell
# To run the web server
; flask --debug run
# Now visit http://localhost:5000/emoji in your browser
```




<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
