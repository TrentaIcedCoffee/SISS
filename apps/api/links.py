from utils.api.decorators import *
from utils.api.res import *
from utils.funcs import *

from ingest.models import *

@login_required
@allowed_methods(['POST'])
def index(request):
    if request.method == 'POST':
        errors, data = posted_data(request, ['ke_id', 'se_id'])
        if errors:
            return bad_request({'error-msg': errors})
        ke, se = get_object_or_404(KualiEntry, id=data['ke_id']), \
                 get_object_or_404(SunapsisEntry, id=data['se_id'])
        if ke.ref_sunapsis is not None or se.ref_kuali is not None:
            return bad_request({'error-msg': 'objects linked already'})
        ke.ref_sunapsis, se.ref_kuali = se, ke
        ke.save()
        se.save()
        return ok()