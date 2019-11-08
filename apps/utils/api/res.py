'''\
    respond with 200: ok(data: Optional[Dict])
    respond with 404: not_found() or not_found({'some_words': 'abc'})
    customized response: json_res_of(123, 'customized response')({'zero': '0'})
'''

from django.http import JsonResponse

def json_res_of(status, error=None):
    def res(data={}):
        if type(data) != dict:
            raise ValueError('data must be a dict')
        elif 'error' in data:
            raise ValueError('key error is reserved')
        if error:
            data['error'] = error
        return JsonResponse(data, status=status)
    return res
    
ok = json_res_of(200)
bad_request = json_res_of(400, 'Bad Request')
forbidden = json_res_of(403, 'Forbidden')
not_found = json_res_of(404, 'Object Not Found')
method_not_allowed = json_res_of(405, 'Method Not Allowed')
server_error = json_res_of(500, 'Server Error')