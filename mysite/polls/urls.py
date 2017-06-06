from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<list_id>[0-9]+)$', views.list_contents, name='list_contents'),
    #
    url(r'^(?P<question_id>[0-9]+)/question_contents$', views.question_contents, name='question_contents'),
    # ex: /polls/5/results/
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


   
    
              
]
