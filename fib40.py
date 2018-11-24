def f(nu):
    if(nu<=1):
        return nu
    else:
        return (f(nu-1)+f(nu-2))
nu=int(raw_input())
for i in range(1,nu+1):
    print f(i),
