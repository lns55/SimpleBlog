"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponseRedirect
from .models import Article, Comment

def home(request):
    """Renders the home page."""
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'latest_articles_list': latest_articles_list
        }
    )

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Article Not Found")
    return render(request, 'app/detail.html', {'article': a})

def leave_comment(request, article_id):
    pass

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
