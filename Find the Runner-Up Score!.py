if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = sorted(arr)
    for i in range(n):
        if (a[n-1-i] > a[n-2-i]):
            print(a[n-2-i])
            break