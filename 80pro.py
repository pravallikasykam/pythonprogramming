nu=int(raw_input(""))
di = []
while nu > 0:
    r = nu % 10
    if r & 1 != 0:
        di.append(str(r))
    nu=nu/10
di = reversed(di)
print (" ".join(di))
