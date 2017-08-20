from django.http import HttpResponse
from django.db.models import Count, Max
from .models import Sample


def index(request):
    obj = Sample(content='asdf')
    obj.save()
    obj.delete()
    return HttpResponse()
