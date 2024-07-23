"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views



urlpatterns = [
    # Home page
    path('', views.index, name='index'),  # Home page URL pattern
    
    # Show all topics
    path('topics/', views.topics, name='topics'),  # Topics page URL pattern
    
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # Single topic detail page URL pattern

    #page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  

    #page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    #delete a topic
    path('topic/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),

] 
      
 

