from utils.decorators import *
from django.http import HttpResponse
from django.conf import settings

import os

@login_required
@allowed_methods(['GET'])
def sample(request):
    path = os.path.join(settings.FILES_ROOT, 'sample.xlsx')
    response = HttpResponse(open(path, 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="sample.xlsx"'
    return response