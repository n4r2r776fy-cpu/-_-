from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    # One-to-one зв'язок (один коментар до одного медіа)
    media = models.OneToOneField(Media, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)