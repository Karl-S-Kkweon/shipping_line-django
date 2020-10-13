# 1. Building Applications

## Creating Apps

```shell
 django-admin startapp [appname]
```

- since app contains multiple functions, appname should be in plural form
- names of .py files in application folder is not optional. You can't change names
- Django makes migration by itself, so we don't have to write sql

```shell
python manage.py makemigrations
python manage.py migrate
```

- Django has database fields for everything: email field, text field... Just call for fields.

---

## Basic Structure of Application

### models.py: All the fields are translated into database stuff.

Models have fields. For the fields you put in models.py, will make be turned into database table. Django ORM translates python code into SQL Instructions to database.

- **[Refer to models.py fields document on Django](https://docs.djangoproject.com/en/2.2/ref/models/fields/).**
- textfield: fields text field without limit on webpage
- charfield: fields text field with limit of single line webpage
- datefield: fields calendar selection on webpage
- boolean field: true of false checkbox

### admin.py: Admin Panel

- **[Refer to admin.py fields document document on Django](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)**
- admin.py regards about admin panel of the website.
- you can create filter(like excel) for fields in table: such as currency or superhost
