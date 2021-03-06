from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^$', views.index),    
    url(r'get_user', views.get_user),   
    url(r'excel', views.excel),    
    url(r'onload', views.onload),    
    url(r'getEmployee', views.getEmployee),    
    url(r'setPeson', views.setPeson),    
    url(r'getPerson', views.getPerson),    
    url(r'showNumLast', views.showNumLast),    
    url(r'reset', views.reset)
]
