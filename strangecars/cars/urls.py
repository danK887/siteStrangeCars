from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/<int:categor_id>/', show_category, name='categories'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('post/<int:post_id>/', show_post, name = 'post'),


]