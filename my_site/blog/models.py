from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f'{self.last_name}, {self.first_name}'

    def __str__(self) -> str:
        return self.full_name()



class Tag(models.Model):
    caption = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.caption



class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image_name = models.FileField(upload_to='images')
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField(Tag)


    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    user_text = models.TextField(max_length=500)


    def __str__(self):
        return f'{self.post.title}, {self.user_name}'

>>>>>>> 0eb7a81 (Blog Website Up and Running)
