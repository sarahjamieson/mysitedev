from django.conf.urls import url
from django.contrib import admin
from pipeline.views import index, get_results, get_samples

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^results/(?P<sample>[-\w]+)/$', get_results, name='results'),
    url(r'^samples/(?P<run>[-\w]+)/$', get_samples, name='samples'),
]
