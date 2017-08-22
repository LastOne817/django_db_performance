from django.http import JsonResponse
from django.db.models import Count, Max
from .models import Sample


def index(request):
    l = Sample.objects.filter(content__startswith='A')
    return JsonResponse(list(l.values('content')), safe=False)
