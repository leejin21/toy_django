# django crash course for beginners

## 1. environment settings

### (1) versions

> versions

| django | python |
| :----: | :----: |
| 3.0.3  | 3.7.6  |

> the way to get django version

```python
import django
django.get_version
```

### (2) start django project

At the terminal(I did this in vs code terminal)
at directiry django

```cmd
django-admin startproject tutorial
```

and this makes django\tutorial and all that.

tutorial\tutorial\ is basically a root directory which includes

-   settings.py
-   urls.py
-   wsgi.py

wsgi.py has codes about how to run my server.

Also, rename the upper `tutorial` directory to `src`

### (3) make database(sqlite)

Type the following at vs code terminal

```cmd
python manage.py migarate
```

and you will see db.sqlite3 right under the src directory.

### (4) start django server

Type the following at vs code terminal

```cmd
python manage.py runserver
```

> Also, I moved the directory src just to organize my django projects nicely. I moved this src directory just under crash1hr folder and I checked if the server run is okay, and it turned out to be okay.

### (5) look around inside of tutorial directory

-   settings.py
    This should be included in .gitignore, because of the secret key and the debug thing.

### (6) start an app

```cmd
python manage.py startapp posts
```

This will make src\posts and all that.

### ending the setups

Django helps you to make your project easier.

## 2. Starting to make an app

Before writing all these codes, you need to edit INSTALLED_APPS in src\tutorial\settings.py.

```python
INSTALLED_APPS = [
    # 아래는 편의상 생략함
    '...',
    # following line is the one you should add
    'posts',
]

```

이걸로 django가 앱을 실행할 때 post를 look할 수 있다.

### (1) Post model 생성하기

models.py에서 아래와 같이 적어준다.

```python
from django.db import models


# following is the codes you need to add
class Post(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

```

이후 cmd 창에서 src 디렉토리 아래서

```cmd
python manage.py makemigrations
```

이렇게 적어두면

```
Migrations for 'posts':
  posts\migrations\0001_initial.py
    - Create model Post
```

posts\migrations\0001_initial.py가 생기는데, 이는 django에게 migration을 할 준비가 되었다는 의미라고 한다.

따라서 다음 코드로 database에 Post를 넣는다.

```cmd
python manage.py migrate
```

### (2) Super User 계정 만들어주기

super user는 모든 게시물들을 관리하는 메니저로, db에 오고가는 정보들을 확인할 수 있다.
