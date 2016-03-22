
from django.conf.urls import url
from django.contrib import admin
from main.views import HomeTemplate

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[\w-]+)/$', 'main.views.current'),
    url(r'^$', HomeTemplate.as_view()),
]
