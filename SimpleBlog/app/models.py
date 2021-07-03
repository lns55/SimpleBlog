"""
Definition of models.
"""

from django.db import models

class Article(models.model):
    article_title = models.CharField("Article Name", max_lenght = 200)
    article_text = models.TextField("Article Body")
    pub_date = models.DateTimeField("Date of publication")

class Comment(models.model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField("Author", max_lenght = 50)
    comment_text = models.CharField("Comment Body", max_lenght = 200)