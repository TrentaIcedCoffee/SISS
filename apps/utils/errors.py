from django.http import HttpResponse

# customized error: error_of(123, 'Customized Error (123)')('a new error')
# predefined error: not_found('this object is not found') or not_found()
def error_of(status_code, error_name):
    def res(message=''):
        context = f'<h1>{error_name}</h1><p>{message}</p>'
        return HttpResponse(context, status=status_code)
    return res

bad_request = error_of(400, 'Bad Request (400)')
not_found = error_of(404, 'Object Not Found (404)')
method_not_allowed = error_of(405, 'Method Not Allowed (405)')
server_error = error_of(500, 'Server Error (500)')

class ServerError(Exception):
    pass