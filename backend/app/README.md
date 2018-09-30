# Faceduck

## Project Structure

Faceduck uses Flask's [`Blueprint`](http://flask.pocoo.org/docs/1.0/blueprints/) feature to moduliarize code.

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