from django.db import models

class Episode(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    upload = models.FileField(upload_to='uploads/', default="default.pdf", blank=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment