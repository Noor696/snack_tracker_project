* ORM : use same implimentaion for diff. SQL lang. for multiple data base.

* each db table consider as a model
* the model write in (app folder -> models.py )

______________________
from django.contrib.auth import get_user_model

# Create your models here.

# each teble represent as a class in the model

class Snack(models.Model):

    # the snack table should contains :
    # 1. the name of snack
    # 2. the rank of snack
    # 3. the purchaser 
    # 4. the description 
    # 5. Id : is auto created by data base

    # now build the scema: the scema is represent the strucure of data base (how the table is look like in db)
    # help_text="" --> this optional
    # the purchaser should be the forign key from the user table

    name = models.CharField(max_length=255,help_text="the name of snack")
    rank = models.IntegerField()
    description = models.TextField(default="description")
    purchaser = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)  # CASCADE means if I delete any user it will delete any data refer to this user from another table


    # then, I want to add the above update on the file of db by add this command:
    # `python manage.py makemigrations`
    # then we find new file create in migrations name : <specific serial number>_initial.py , and this file take the snack from the model
    # migration means the changes in the data base
    # then write this command to apply the new migration into db:
    # `python manage.py migrate`

    # then go to admin.py to regester the model

    # when edit any table you shold to repeat the two command:
    # `python manage.py makemigrations` --> `python manage.py migrate`

    def __str__(self):
        # to see the name of object
        return self.name

______________________

------> go to admin.py file in app folder and regester the model

from .models import Snack

# Register your models here.

admin.site.register(Snack)

---------------------

------> make template to show the table to the user

1. make path in urls.py inside app folder (snackes)
2. make class for the path in view.py inside app folder (snackes)

_____________________

we can make the data base design by using site: and it is the **first step** in backend to determine the kind of the data we have it inside the application. 
specify: the name of tables, the releations between tables, specify the primary key, forign key, ...

**app.sqldbm.com**