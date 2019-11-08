from utils.api.decorators import *
from utils.api.res import *
from utils.funcs import *
from rest_framework import serializers

from ingest.models import KualiEntry

class KualiEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = KualiEntry
        fields = '__all__'
    
@login_required
@allowed_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        kes = KualiEntry.objects.all()
        return ok({'data': KualiEntrySerializer(kes, many=True).data})
        
@login_required
@allowed_methods(['GET', 'DELETE'])
def id(request, ke_id):
    if request.method == 'DELETE':
        ke = get_object_or_404(KualiEntry, id=ke_id)
        ke.delete()
        return ok()
    elif request.method == 'GET':
        ke = get_object_or_404(KualiEntry, id=ke_id)
        return ok({'data': KualiEntrySerializer(ke).data})