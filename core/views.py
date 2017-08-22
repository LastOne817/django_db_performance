from django.http import JsonResponse
from django.db.models import Count, Max
from .models import Sample
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    l = Sample.objects.filter(content__startswith='A')
    return JsonResponse(list(l.values('content')), safe=False)
