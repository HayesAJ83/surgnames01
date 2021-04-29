# Python + Flask and Bootstrap

[ ![Codeship Status for lvlds/heroku-flask-bootstrap](https://app.codeship.com/projects/9528e3a0-0823-0135-eb1e-6e6e4a78e626/status?branch=master)](https://app.codeship.com/projects/214278)

A Python application using [Flask](http://flask.pocoo.org/) and [Bootstrap](https://getbootstrap.com/)

**Demo** [is running here 🚀🚀🚀](https://vast-harbor-38662.herokuapp.com/)

## Running Locally
Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku CLI](https://cli.heroku.com/) installed.

```sh
$ git clone git@github.com:lvlds/heroku-flask-bootstrap.git
$ cd heroku-flask-bootstrap

$ pip install -r requirements.txt

$ python app.py

# or run locally with heroku

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku open
```
or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)