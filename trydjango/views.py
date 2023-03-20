"""
To render html web pages 
"""
import random
from django.http import HttpResponse

from articles.models import Article 

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response) 
    """

    name = "Avinash"
    random_id = random.randint(1,3)
    article_obj = Article.objects.get(id=random_id)

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    #Django Templates
    HTML_STRING = """
    <h1>{title} ({id})!</h1>
    <p>{content}</p>
    """.format(**context)

    return HttpResponse(HTML_STRING)