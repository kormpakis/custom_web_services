# custom_web_services
A project using Flask Framework and connects Android with Wordpress
## Install MySQL Client
+ Install Wheel: pip install wheel
+ Download from ![here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
+ pip install mysqlclient-1.3.13-cp37-cp37m-win_amd64.whl

## Install Flask
+ pip install flask

## Install requests
+ pip install requests

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
```
GET /user/1/tag/9/interests/ 

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
```
GET /post/409/info/

{
    "items": {
        "image_url": "",
        "post_url": "http://localhost/wordpress/2018/08/telikos/",
        "title": "telikos"
    }
}
```
```
GET /user/1/tags/info/ 

{
    "items": [
        {
            "count": 27,
            "tag": 5
        },
        {
            "count": 73,
            "tag": 4
        },
        {
            "count": 10,
            "tag": 9
        },
        {
            "count": 23,
            "tag": 2
        }
    ]
}

```
```
GET /user/1/selected/posts/ 

{
    "items": [
        {
            "post_id": 409,
            "priority": 1
        }
    ]
}

```
For all requests that don't exist, it returns the following message
```
{
    "items": {
        "response": "Not found"
    }
}
```