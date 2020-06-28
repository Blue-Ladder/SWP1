from template import html

def application(environ, start_response): 
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0] 
  
	if '' not in [a, b]:        
                a, b = int(a), int(b)
		X = a+b
		Y = a*b
	else:
		X = 'Please input both x and y'
		Y = 'Please input both x and y'
	response_body = html % {'x + y':X, 'x * y':Y}


        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]

