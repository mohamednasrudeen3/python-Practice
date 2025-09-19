def sq_num(n):
    sq =[]
    for i in range(1,n+1):
        sq.append(i*i)
    return sq

print(sq_num(7))


def sq_num_gen(n):
    for i in range(1,n+1):
        yield i*i


gener =sq_num_gen(7)
print(gener)

for i in gener:
    print(i, end=" ")