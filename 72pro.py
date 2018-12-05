l=raw_input("")
v=set('aeiou')
if not v.isdisjoint(l):
    print "yes"
else:
    print "no"
