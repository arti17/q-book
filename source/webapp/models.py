from django.db import models

STATUS_ACTIVE = 'active'
STATUS_CHOICES = (
    (STATUS_ACTIVE, 'Active'),
    ('blocked', 'Blocked'),
)


class Entry(models.Model):
    author = models.CharField(max_length=40, verbose_name='Author')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Text')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Edit date')
    status = models.CharField(max_length=20, default=STATUS_ACTIVE, choices=STATUS_CHOICES, verbose_name='Status')

    def __str__(self):
        return f'{self.author} - {self.email} - {self.text} | {self.create_date} | {self.status}'
