from utils.decorators import *
from utils.routes import *
from ingest.models import KualiEntry, SunapsisEntry

@allowed_methods(['GET'])
@login_required
def index(request):
    titles_kuali = 'doc_id,tracking_id,fullname_kuali,amount_kuali,date_kuali'.split(',')
    titles_sunapsis = 'doc_id,sunapsis_id,fullname_sunapsis,amount_sunapsis,date_sunapsis'.split(',')
    return render(request, 'match/index.html', {
        'kes': KualiEntry.objects.filter(ref_sunapsis=None), 
        'ses': SunapsisEntry.objects.filter(ref_kuali=None),
        'titles_kuali': titles_kuali,
        'titles_sunapsis': titles_sunapsis,
    })