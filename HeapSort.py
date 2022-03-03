import time

def HeapSort(A):
    Build_MH(A)
    le = len(A)-1
    heapsize = le
    for i in range(le, 2, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        heapsize = heapsize - 1
        Max_Heapify(A, 1)

def Build_MH(A):
    le = len(A)-1
    half = int(le/2)
    for i in range(half, 1, -1):
        Max_Heapify(A,i)

def Max_Heapify(A,i):
    l = left(i) #Left child to the parent in the heap
    r = right(i) #To find the right child to the parent in the heap
    if (l <= heapsize and A[l] > A[i]): #checking to see if left child > parent
        largest = l 
    else: 
        largest = i
    
    if (r <= heapsize and A[r] > A[largest]): #checking to see if right child > parent
        largest = r
    
    if (largest != i):
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest)
    
def parent(i):
    return i/2

def left(i): #To find the left child to the parent in the heap
    return 2 * i

def right(i): #To find the right child to the parent in the heap
    return 2 * i + 1

def ReadFile(name): #used to read file
    file = open(name)
    A = file.read().split()
    return A

B = ["100.txt", "1000.txt", "5000.txt", "50000.txt", "100000.txt"] #input files
for i in B:
    f = ReadFile(i)
    
    start = time.time()
    heapsize = len(f)
    HeapSort(f)
    end = time.time()
    
    t = end-start
    
    print(i, " time: ", t)


