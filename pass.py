for s in range (10):
    if s% 20==0:
        print("twist")
    elif s% 15==0:
        pass
    elif s% 5==0:
        print("buzz")
    elif s% 3==0:
        print("fizz")
    else:
        print(s)