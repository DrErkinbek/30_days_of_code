if __name__ == '__main__':
    n = int(input().strip())
    dic = {}
    for i in range(n):
        name, phone = input().strip().split()
        dic[name] = int(phone)
try:
    while True:
        query = input().strip()
        query_result = "Not found" if query not in dic else query + "=" + str(dic[query])
        print(query_result)
except EOFError:
    pass