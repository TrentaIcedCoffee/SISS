from utils.api.decorators import *
from utils.api.res import *
from utils.funcs import *
from rest_framework import serializers

from ingest.models import SunapsisEntry

class SunapsisEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SunapsisEntry
        fields = '__all__'
    
@login_required
@allowed_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        kes = SunapsisEntry.objects.all()
        return ok({'data': SunapsisEntrySerializer(kes, many=True).data})
        
@login_required
@allowed_methods(['GET', 'DELETE'])
def id(request, se_id):
    if request.method == 'DELETE':
        se = get_object_or_404(SunapsisEntry, id=se_id)
        se.delete()
        return ok()
    elif request.method == 'GET':
        se = get_object_or_404(SunapsisEntry, id=se_id)
        return ok({'data': SunapsisEntrySerializer(se).data})