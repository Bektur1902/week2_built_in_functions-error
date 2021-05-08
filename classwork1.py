
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)

a = []

for i in values:
	try:

	    if set(i) == True:
		    a.append(True)
	    else:
		    a.append(False)

	except TypeError:
		print(all(a), end = ' ')
