from django.db import models


class Image(models.Model):
    picture = models.ImageField()
    classify = models.CharField(max_length=100, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'image classified at {}'.format(self.uploaded.strftime('%Y/%m/%d %H:%M'))

    def save(self, *args, **kwargs):
        try:
            print('success')
        except:
            print('classification failed')
        super().save(*args, **kwargs)