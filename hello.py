# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
#                   encoding="utf8")]
def app(environ, start_response):
    data = ''
    for line in environ["QUERY_STRING"].split("&"):
        data = data+line+"\n"
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [data]