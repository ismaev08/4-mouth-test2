from django.db import models

class Books(models.Model):
    GENRE_CHOICES =(
        ("ужасы", "ужасы"),
        ("комедия", "комедия"),
        ('фантастика', "фантастика")
    )
    image = models.ImageField(upload_to="movies/", verbose_name=" загрузите фото ")
    title = models.CharField(max_length=100, verbose_name=" укажите название книги ")
    description = models.TextField(verbose_name="описание книги", blank=True)
    price = models.PositiveIntegerField(verbose_name=" укажите цену ", default="400")
    create_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name="выберите жанр")
    gmail = models.CharField(max_length=100, verbose_name= "укажите почту автора")
    director = models.CharField(max_length=100, verbose_name="укажите имя автора", default="Селим исмаев")
    trailer = models.URLField(verbose_name="укажите ссылку с ютуба")

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"


    def __str__(self):
        return f'{self.title}:{self.price}'


