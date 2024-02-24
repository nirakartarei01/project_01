# comapny project managemnt 
  This project having user creation forms with auth and task management and communication

  Setup of this project
To get this repository, run the following command inside your git enabled terminal

$ git clone 


Once you have downloaded django, go to the cloned repo directory and run the following command

$ python manage.py makemigrations

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command

$ python manage.py migrate
type the following command and provide username, password and email for the admin user

$ python manage.py createsuperuser

 can start using our simple todo App. Start the server by following command

$ python manage.py runserver
Once the server is hosted, head over to http://127.0.0.1:8000/


