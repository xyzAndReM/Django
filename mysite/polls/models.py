from django.db import models

class List(models.Model):
    def __str__(self):
        return self.list_text
    list_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')


class Question(models.Model):
    def __str__(self):
        return self.question_text
    lista = models.ForeignKey(List,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_text2 = models.CharField(max_length=500,default='Questao vazia')
    question_text3 = models.CharField(max_length = 50,default = '0')
    image = models.ImageField(upload_to="images")
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)