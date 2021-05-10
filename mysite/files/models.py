from django.db import models


class File(models.Model):
    csv_file = models.FileField(upload_to="myfiles")
