s=raw_input()
"""if all(j in '01' for a in s):
    print "yes"
else:
    print "No"
    """
if not(s.translate(None,'01')):
    print "yes"
else:
    print "No"
