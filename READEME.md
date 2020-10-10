# Shipping_Line-Django

## Django Project Folder & File Structure

- [config folder](./config) is master folder
- rest of folders are just applications: applications are group of functionalities.

## [Project configuration folder's](./config) structure

- settings.py: you can refer to installed default apps in django. Look at django documentation links to find out.
- init.py helps to work like python package
- urls.py: controls url of the website. Can also be established under application.

## Individual application folders' structure

- apps.py: configuration file which is installed [at the project's settings.py](./config/settings.py)
- models.py: describing how database look like.
- admin.py: reflects changes on models.py to admin panel
- views.py: function that renders html
- urls.py: you can create urls.py under an application.like /users/profile, /users/delete, /users/register etc.

## Our development environment

### Gyeonghun Park

- System: Mac OS Catalina 10.15.7 (19H2)
- Python 3.8.6 64-bit
- Django 3.1.2
