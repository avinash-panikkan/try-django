"""
To render html web pages 
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article 

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response) 
    """
    
    name = "Avinash"
    random_id = random.randint(1,4)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    contexts = {
        "object_list": article_queryset,
        "object":article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    #Django Templates
    HTML_STRING = render_to_string("home-view.html",context=contexts)
    # HTML_STRING = """
    # <h1>{title} ({id})!</h1>
    # <p>{content}</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)