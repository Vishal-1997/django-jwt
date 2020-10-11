from django.conf import settings
from django.core import serializers
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from caching.models import UserDetails

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET'])
def without_cache(request):
    data = serializers.serialize("json", UserDetails.objects.all())
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@cache_page(CACHE_TTL)
def per_view_cache(request):
    data = serializers.serialize("json", UserDetails.objects.all())
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def per_data_cache(request):
    if 'user_list' in cache:
        user_list = cache.get("user_list")
        return Response(user_list, status=status.HTTP_200_OK)
    else:
        data = serializers.serialize("json", UserDetails.objects.all())
        cache.set("user_list", data, timeout=CACHE_TTL)
        return Response(data, status=status.HTTP_200_OK)



