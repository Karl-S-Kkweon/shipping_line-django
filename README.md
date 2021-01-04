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

## Team development environment

- Python 3.8.6 64-bit
- Django 3.1.2

### + Gyeonghun Park

- System: Mac OS Catalina 10.15.7 (19H2)

### + Soonyeong Kweon

- System: Windows 10 Education (Build 1909)


## Update Logs

- Project Initialization & Setup. -- by G. Park, 10-10-2020 

- Created tables; owners & hulls. -- by G. Park, 10-13-2020  

- Tested Fork and Pull Request -- by S. Kweon, 10-13-2020

- Updated on tables; owners & hulls. -- by G. Park, 10-14-2020

- Migrations. -- by G. Park, 11-02-2020 

- Newly Forked and cloned, add a remote 'upstream' for G. Park's repository -- by S. Kweon, 12-05-2020

- Updated on a table; hulls . -- by G. Park, 12-05-2020

- Added function on a table; hulls . -- by G. Park, 12-06-2020

- Created Hull_Report model -- by S. Kweon, 12-20-2020

- Updated readme -- by G. Park, 12-23-2020

- Modified Hull_Report url -- by S. Kweon, 12-23-2020

- Added a table; Warranty_Details -- by S. Kweon, 12-30-2020

- Fixed DB data -- by S. Kweon, 12-30-2020
    * deleted useless table, 'hulls_owners'
    * add 'owner_id' column to 'hulls' table, then filled 'owner_id' column with sample data

- Updated Warranty_Details -- by S. Kweon, 12-31-2020

- Added Tables and sample data -- by S. Kweon, 01-01-2021
    * add 3 tables: manufacturers, yard_departments, gitand communication_logs
    * add sample data for manufacturers and yard departments

- Added a Table and a simple DB diagram -- by S. Kweon, 01-02-2021
    * add 1 table: relevant_groups
    * add a simplified DB diagram to show relatinoships among tables; yard_depts, manufacturers, and        relevant groups.

- Updated readme -- by S. Kweon, 01-03-2021