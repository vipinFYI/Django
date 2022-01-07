from django.db import models
from django.utils import timezone

"""
user_directory_path uses instance and filename identify a path for the image
instace allow us to utlize our item.
output - media/posts/user_id/filename

"""
def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.id, filename)


class Post(models.Model):

    title = models.CharField(max_length=250)
    # we can alternatively give default path if wish to use in upload_to
    image = models.ImageField(
        upload_to=user_directory_path)
    image_caption = models.CharField(
        max_length=100, default='Photo by demo')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title