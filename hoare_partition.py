def hoare_partition(a, low, high):
    pivot = a[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        j -= 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

def quick_sort_iterative(a):
    size = len(a)
    stack = []
    stack.append((0, size-1))
    while stack:
        low, high = stack.pop()
        if low < high:
            p = hoare_partition(a, low, high)
            stack.append((low, p))
            stack.append((p+1, high))

def main():
    a = [10,7,8,9,1,5,3,6,2,4]
    print("Before", a)
    quick_sort_iterative(a)
    print("After", a)

if __name__ == "__main__":
    main()
