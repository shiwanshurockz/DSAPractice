def simplified(exp):
    n = len(exp)
    res = [None] * n
    s = []
    s.append(0)
    index = 0
    i = 0
    while i < n:
        if exp[i] == "-":
            if s[-1] == 1:
                res.append("+")
                index += 1
            elif s[-1] == 0:
                res.append("-")
                index += 1
        elif exp[i] == "+":
            if s[-1] == 1:
                res.append("-")
                index += 1
            elif s[-1] == 0:
                res.append("+")
                index += 1
        elif exp[i] == "(" and i > 0:
            if exp[i-1] == "-":
                z = 0 if s[-1] == 1 else 1
                s.append(z)
            if exp[i-1] == "+":
                z = 0 if s[-1] == 0 else 1
                s.append(z)
        elif exp[i] == ")":
            s.pop()
        else:
            res.append(exp[i])
            index += 1
        i+=1
    return res


expr = "a-(b-c-(d+e))-f"
res = simplified(expr)
res = "".join([i for i in res if i is not None])
print(res)
