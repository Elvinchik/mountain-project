from django.db import models


class CommentsInMaldiv(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return str(self.id)
