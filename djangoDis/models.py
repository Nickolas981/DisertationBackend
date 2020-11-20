
from django.db import models


conditions = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
}

class Product(models.Model):
    name = models.CharField(max_length=200)
    item_condition_id = models.IntegerField(default=5)
    category_name = models.CharField(max_length=1000, default="")
    brand_name = models.CharField(max_length=200, default="")
    price = models.CharField(max_length=12, default="")
    shipping = models.BooleanField(default=False)
    item_description = models.CharField(max_length=2000, default="")


