from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^destroy_session$', views.destroy_session),
    url(r'^process_money$', views.process_money),

]