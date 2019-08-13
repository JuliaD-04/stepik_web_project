                                                   

def application(environ, start_response):
                                                          
		
	status = '200 OK'

	headers = [
		('Content-Type', 'text/plain'),
	]
	body = "Hello world!"
	start_response(status, response_headers)                                    

	return [body]