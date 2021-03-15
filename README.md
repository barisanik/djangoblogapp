# Django Blog App
This is a simple blog file which is made with django-admin 3.1.5, django-crispy-forms 1.10.0 and Python 3.8.2rc2 versions while building. Also I am using sqlite3 database.

# Starting Blog App
To start blog app you need to use a cmd, powershell or another terminal.
1. Go to blog file directory in terminal.
2. Install django-admin, django-crispy-forms with pip install command.
3. Run this command: python manage.py runserver your_ipv4_adress
!your_ipv4_adress part is not necessary if you gonna run for local. Without that part, it will be start on 127.0.0.1:8000 adress.
! If you want to run into LAN you must know your ipv4 adress. You can learn it from cmd with ipconfig command. Then you have to add it into Allowed Hosts from settings.py file. And also, you should write runserver command with ipv4 adress.
