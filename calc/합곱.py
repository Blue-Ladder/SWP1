from cgi import parse_qs
from template import html

def application(environ, start_response): 
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0] 
  
	try:        
                a, b = int(a), int(b)
		X = a+b
		Y = a*b
	except ValueError:
		X = 'Please input both x and y. You can only input integer'
		Y = 'Please input both x and y. You can only input integer'
	response_body = html % {'x + y':X, 'x * y':Y}


        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]
