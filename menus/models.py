from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=200, blank=True, verbose_name="URL")
    named_url = models.CharField(
        max_length=100, blank=True, verbose_name="Именованный URL")
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
        verbose_name="Родительский пункт"
    )
    menu_name = models.CharField(max_length=100, verbose_name="Название меню")

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ["menu_name", "title"]

    def __str__(self):
        return self.title
