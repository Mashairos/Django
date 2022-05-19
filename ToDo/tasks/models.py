from django.db import models
from django.contrib.auth import get_user_model

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS,)
    # Chave Estrangeira para identificar o usuário no Login: 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # Dados Preenchidos pelo Sistema:
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title