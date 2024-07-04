import sys
n = (int)(sys.argv[1])
m = (int)(sys.argv[2])

list_res = [1]
while True:
    list_res.append((list_res[-1]+(m-1)) % n)
    if list_res[0] == list_res[-1]:
        break
    
list_res.pop()
list_res = [n if x == 0 else x for x in list_res]

print("".join([str(x) for x in list_res]))
