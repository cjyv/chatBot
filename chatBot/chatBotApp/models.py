from django.db import models

# Create your models here.
#models.py(データベースと連動)

class Contact(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=30)
    phone = models.IntegerField()
    comment = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'contact'
