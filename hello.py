                                                   
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return (body)

    # return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
    #               encoding="utf8")]





    # def application(environ, start_response):
                                                          
		
# 	status = '200 OK'

# 	headers = [
# 		('Content-Type', 'text/plain'),
# 	]
# 	body = "Hello world!"
# 	start_response(status, response_headers)                                    

# 	return [body]