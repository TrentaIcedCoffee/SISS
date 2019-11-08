from utils.decorators import *
from utils.routes import *
from utils.messages import *
from utils.errors import *

from .utils import *

@allowed_methods(['GET', 'POST'])
@login_required
def index(request):
	if request.method == 'GET':
		return render(request, 'ingest/index.html')
	elif request.method == 'POST':
		try:
			excel = request.FILES.get('excel', None)
			if not excel:
				raise FileError().with_message(request, 'no file has been uploaded')
			if not excel.name.endswith('.xlsx'):
				raise FileError().with_message(request, 'File is not in Excel type')
			if excel.multiple_chunks():
				raise FileError().with_message(request, f'File is too big {csv_file.size/(1000*1000):.2f}MB')
			path = upload_file(request, excel)
			validate_excel(request, path)
			compose(request, path)
			messages.success(request, 'data ingested')
			return redirect('ingest:index')
		except FileError as _:
			return redirect('ingest:index')
		except Exception as e:
			return server_error(str(e))