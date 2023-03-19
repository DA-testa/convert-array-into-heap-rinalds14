# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n//2, -1, -1):
        j = i
        while True:
            k = j*2 + 1
            if k >= n:
                break
            if k+1 < n and data[k+1] < data[k]:
                k += 1
            if data[j] <= data[k]:
                break
            swaps.append((j, k))
            data[j], data[k] = data[k], data[j]
            j = k
    return swaps


def main():
    inputs=input()
    if "I" in inputs:
        n = int(input())
        data = list(map(int, input().split()))
     elif "F" in inputs:
        f=input()
        with open("tests/" + f, 'r') as f:
            n=int(f.readline())
            data=list(map(int, f.readline().split()))


    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
