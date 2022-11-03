n=int(input())
if n>=0:
    print(int(str(n)[::-1]))
else:
    n=-n
    print(-1*int(str(n)[::-1]))