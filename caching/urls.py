from django.conf.urls import url
from django.views.decorators.cache import cache_page

from caching.views import without_cache, per_view_cache, per_data_cache

urlpatterns = [
    url(r'without-cache/$', without_cache),
    url(r'with-cache-url/$', cache_page(60 * 15)(without_cache)),
    url(r'per-view-cache/$', per_view_cache),
    url(r'per-data-cache/$', per_data_cache),
]
