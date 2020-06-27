from cgi import parse_qs
from template import html

def application(environ, start_response): 
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0] 
  
        if '' not in [a, b]:
                a, b = int(a), int(b)
		X = a+b
		Y = a*b
        	response_body = html % {
	    	'x + y': X,
	    	'x * y': Y,
		}
	else:
		A = ''
		B = ''
		response_body = html % {
	    	'x + y': A,
	    	'x * y': B, 
		} 

        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]

