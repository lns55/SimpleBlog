"""
Definition of models.
"""

from django.db import models

class Article(models.Model):
    article_title = models.CharField('Article Name', max_length = 200)
    article_text = models.TextField("Article Body")
    pub_date = models.DateTimeField("Date of publication")

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Author', max_length = 50)
    comment_text = models.CharField("Comment Body", max_length = 200)