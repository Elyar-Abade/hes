from django.db import models

# Create your models here.

class Reaction(models.Model):
    reaction = models.BooleanField(null=True)
    def __str__(self):
        return str(self.reaction)
    
    
class Item(models.Model):
    item = models.CharField(max_length=30)
    reactions = models.ForeignKey(Reaction, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.item
    

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    reactions = models.ForeignKey(Reaction, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.comment