"""Defines URL patterns for learning_logs."""

from django.urls import path                    # path; function that creates url patterns
from . import views
app_name = 'learning_logs'                      # a variable that helps Django distinguish this ...
                                                # ... urls.py from other urls.py with in the project

urlpatterns = [                                 # urlpatterns sends "requests" to the related views.functions.
    # Home page                                     
    path('', views.index, name='index'),        # Passing a 'request object' to index() function
    # Page that shows all topics.                   
    path('topics', views.topics, name='topics'),# with assigning name index to a URL, to make easier
    # Detail page for a single topic.           # ... referring to other files throughout the project.
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # topic_id; a parameter's value is sent to topic().                                           
    # Page for adding a new topic.                              # (x:y; match x and assign it to y)
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), 
    ]                                                        