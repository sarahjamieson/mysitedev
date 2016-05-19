from django.conf.urls import url
from django.contrib import admin

from genesearch.views import gene_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/$', gene_search, name='search'),
]