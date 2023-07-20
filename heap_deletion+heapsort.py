# def maxheap(heap,n,i):
#
#     L = 2*i+1
#     R = 2*i+2
#
#     if L < n and heap[i] < heap[L]:
#         largest = L
#     else:
#         largest = i
#
#     if R < n and heap[largest] < heap[R]:
#         largest = R
#
#     if largest != i:
#         heap[largest],heap[i] = heap[i],heap[largest]
#         maxheap(heap,n,largest)
#
#     return
#
# def delete_element(heap,n):
#
#     while(n!=0):
#         heap[0],heap[n-1] = heap[n-1],heap[0]
#         n =n -1
#         maxheap(heap,n,0)
#
#     return heap