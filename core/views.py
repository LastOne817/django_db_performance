from django.http import JsonResponse
from django.db.models import Count, Max
from .models import Sample

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    l = Sample.objects.filter(content__startswith='A')
    return JsonResponse(list(l.values('content')), safe=False)
