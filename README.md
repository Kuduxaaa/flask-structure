# FlaskInit

This is an already built-in MVC structure for Flask application, you can add models views and controllers, you can also easily start working on the API with a structure already made

```
- app
    - api
        - __init__.py
        - resources.py


    - controllers
        - main.py


    - models
        - users.py


    - public
        - css
        - img
        - js
        - robots.txt


    - service
        - __init__.py


    - views
        - error
        - inc
        - layouts
        - main

    - __init__.py

- config.py
- requirements.txt
- manager
```

## API Folder

From here you can add as many resources as you want for API. Do not forget to register these resources in the `__init __.py` file.

```python3
from app.api import resources, RESOURCE_FILE    # API Resources

api_router.add_resource(resources.Example, '/')
api_router.add_resource(RESOURCE_FILE.RESOURCE_CLASS_NAME, 'RESOURCE_ROUTE')
```
