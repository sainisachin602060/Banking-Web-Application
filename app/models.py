from django.db import models




class customer(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    balance=models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    
class history(models.Model):
    sender=models.CharField(max_length=200)
    reciever=models.EmailField(max_length=100)
    amount=models.IntegerField()
    
    def __str__(self):
        return self.sender    
    
    

    
        
    
    