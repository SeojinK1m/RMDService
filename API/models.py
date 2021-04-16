from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=60)

class Eatery(models.Model):
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    name = models.CharField(max_length=120)
    url = models.CharField(max_length=60)
    class EATERY_TYPE(models.TextChoices):
        restaurant = 'res'
        dining_hall = 'din'
    eatery_type = models.TextField(choices = EATERY_TYPE.choices)  

class Review(models.Model):
    eatery = models.ForeignKey(Eatery, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    comment = models.TextField()
    class REVIEW_CHOICES(models.IntegerChoices):
        very_good = 5
        good = 4
        average = 3
        meh = 2
        yuck = 1
    numeric_review = models.IntegerField(choices = REVIEW_CHOICES.choices)
