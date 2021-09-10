from django.db import models

from cmsapp.model_utils import BaseModel


person_type = [
    (0, 'Participant'),
    (1, 'Speaker'),
]


class Conference(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date']


class Person(BaseModel):
    username = models.CharField(max_length=255)
    email_id = models.EmailField(max_length = 255)
    person_type = models.IntegerField(choices=person_type, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']


class Talk(BaseModel):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, null=False, related_name='talk')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    people = models.ManyToManyField(Person)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
