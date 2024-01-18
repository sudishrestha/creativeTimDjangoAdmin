### Installation
- Create virtual env and activate for enviornment isolation (Optional)
- pip install requirements.txt
- change your database username,name and password in settings.py
- change you gmail email and app password in reviewSystem\backend\serializer.py

### Create your user
create superuser with python manage.py createsuperuser
- go to yourhost/admin
- login 
- create user and respective user access/group

### Test api
Api url are:
- your_host/api/shop/
- your_host/api/review/

##### Test from postman
- import collection to postman
- adjust your credential from authorization

