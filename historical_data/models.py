from django.db import models

# Create your models here.
class PriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=3)


# removing a migration

# use pyhton manage.py showmigrations
# this will produce all the migrations and give you the migrations names
# NEXT
# python manange.py migrate 0001_name_of_migration
#  then we can use the show migration command to see if it worked or we could use the dbshell to check


#To name migrations
# python mananage.py makemigration historical_data --name then_the_name_you_want
