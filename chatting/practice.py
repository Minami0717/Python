alpa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
while True:
    w = input()
    for a in alpa:
        w = w.replace(a,'?')
    print(len(w))
    print(w)
