def kthLargestElement(nums, k):
    heap = MinHeap()
    for num in nums:
        if len(heap) < k:
            heap.push(num)
        elif len(heap) == k and num > heap.peek():
            heap.push(num)
        if len(heap) > k:
            heap.pop()
    # print(heap.heap)
    return heap.pop()


class MinHeap(object):
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0]

    def push(self, item):
        self.heap.append(item)
        self.sink(len(self.heap) - 1)

    def pop(self):
        val = self.heap[0]
        if len(self.heap) == 1:
            return self.heap.pop()
        self.heap[0] = self.heap.pop()
        i = self.swim(0)
        self.sink(i)
        return val

    def swim(self, ind):
        left_ind = ind*2 + 1
        right_ind = ind*2 + 2
        if ind*2 + 1 < len(self.heap):
            if right_ind < len(self.heap):
                if self.heap[left_ind] < self.heap[right_ind]:
                    MinHeap.exch(self.heap, ind, left_ind)
                    return self.swim(left_ind)
                else:
                    MinHeap.exch(self.heap, ind, right_ind)
                    return self.swim(right_ind)
            else:
                MinHeap.exch(self.heap, ind, left_ind)
                return self.swim(left_ind)
        else:
            return ind

    def sink(self, ind):
        parent = (ind-1) // 2
        # print(self.heap, ind, parent, self.heap[parent], self.heap[ind])
        if ind > 0 and self.heap[parent] > self.heap[ind]:
            MinHeap.exch(self.heap, ind, parent)
            self.sink(parent)

    @staticmethod
    def exch(l, i, j):
        swap = l[i]
        l[i] = l[j]
        l[j] = swap

# Java
# int kthLargestElement(int[] nums, int k) {
#     //do heap sort
#     PriorityQueue<Integer> minQueue = new PriorityQueue<Integer>(k);
#     for(int i = 0; i< nums.length; i++){
#         minQueue.offer(nums[i]);
#         if(minQueue.size() > k){
#             minQueue.poll();
#         }
#     }

#     return minQueue.peek();
# }