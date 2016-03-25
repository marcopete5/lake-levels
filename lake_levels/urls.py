
from django.conf.urls import url
from django.contrib import admin
from main.views import HomeTemplate
from django.conf import settings 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^(?P<slug>[\w-]+)/$', 'main.views.current'),
    url(r'^home/', 'main.views.lake_API_view'),
    url(r'^$', HomeTemplate.as_view()),
    url(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
