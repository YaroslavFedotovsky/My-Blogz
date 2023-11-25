from django.db import models

#Posts
class Post(models.Model):
    # Information about the post
    title = models.CharField('Heading', max_length=100)
    textContent = models.TextField('Text')
    author = models.CharField('Author', max_length=100)
    date = models.DateField('Date of publication')
    image = models.ImageField('Images', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

#Comments
class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    text_comments = models.TextField('Comment Text', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

#Likes
class Likes(models.Model):
    ip = models.CharField('IP-adress', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)