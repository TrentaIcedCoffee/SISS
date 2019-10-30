from django.shortcuts import get_object_or_404
posted_data = lambda request, keys: {key: request.POST.get(key, None) for key in keys}
