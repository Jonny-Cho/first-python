from django.conf.urls import url
# .은 같은폴더를 의미
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]