# Faceduck

## Project Structure

Faceduck uses Flask's [`Blueprint`](http://flask.pocoo.org/docs/1.0/blueprints/) feature to moduliarize code.
The architecture is inspired in [this one](https://github.com/Robpol86/Flask-Large-Application-Example/).

Right now a single Blueprint for the API has been created. However, as we're using a REST-ful API style, in the future 
we'll be able to modularize and split the `api` blueprint into a blueprint per each resource, for example.

```
/core
/models
/views
```

* `core` folder contains application services to abstract logic away from the controller to a service.

* `models` folder contains domain models that will be used to persist to ES, and (un)marshall from/to JSON for the API.

* `views` folder contain the different blueprints that support our API routes.


## Dependencies

We're using flask-jwt-extended to handle authentication and session keeping. If you have any doubts regarding this 
module, please check its documentation [here](https://flask-jwt-extended.readthedocs.io/en/latest/index.html).

## API Testing

Every new endpoint/feature since the API testing branch should strive to implement new API tests to ensure that
the API has the intended functionality. 

We're using Postman's newman tool to run tests. You can see on the Dockerfile and .travis.yml how everything's executed.

To add new tests, you need to import the json collection in `test/api` into Postman, and there you'll be able to
create new texts. Remember to export and replace the file if you've added more tests.

You can look at the tests tab on each request how everything is working or feel free to ping @ifrins or @efz1005
if you need help. Happy testing!    