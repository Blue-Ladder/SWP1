html = b"""
<html>
    <body>
	<form action="">
	    x = <input type="number" name="a"><br><br> 
	    y = <input type="number" name="b"><br><br>
            <input type="submit">
	</form>
	<p>
	    x + y: %(x + y)s<br>
	    x * y: %(x * y)s<br>
	</p>
    </body>
</html>
"""

