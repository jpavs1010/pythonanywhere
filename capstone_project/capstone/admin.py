from django.contrib import admin

from .models import AccessData
from .models import MapData
from .models import CorrelationData
# Register your models here.

admin.site.register(AccessData)
admin.site.register(MapData)
admin.site.register(CorrelationData)
