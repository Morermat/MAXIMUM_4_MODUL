from django.db import models

class Advetisment(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction =  models.BooleanField('Торг', help_text='Отметьте если вы согласны на торг')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'advertisements'
    def __str__(self): 
        return f'Advertisement(title={self.title}, description={self.description}, price={self.price}, auction={self.auction}, created_at={self.created_at}, update_at={self.update_at})'