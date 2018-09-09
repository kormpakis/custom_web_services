# custom_web_services
A project using Flask Framework and connects Android with Wordpress
## Install MySQL Client
+ Install Wheel: pip install wheel
+ Download from ![here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
+ pip install mysqlclient-1.3.13-cp37-cp37m-win_amd64.whl

## Install Flask
+ pip install flask

## Run webservices
+ flask run

**Examples**
```
GET /interests/ 

{
    "items": [
        {
            "count_tags": 27,
            "tags_id": 5,
            "user_id": 1
        },
        {
            "count_tags": 73,
            "tags_id": 4,
            "user_id": 1
        },
        {
            "count_tags": 10,
            "tags_id": 9,
            "user_id": 1
        },
        {
            "count_tags": 23,
            "tags_id": 2,
            "user_id": 1
        }
    ]
}
```
```
GET /user/2/interests/

{
    "items": [
        {
            "count_tags": 6,
            "tags_id": 4,
            "user_id": 2
        }
    ]
}
```
```
GET /tag/9/interests/ 

{
    "items": [
        {
            "count_tags": 10,
            "tags_id": 9,
            "user_id": 1
        }
    ]
}
```

