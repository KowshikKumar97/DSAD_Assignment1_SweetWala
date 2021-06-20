import sys
class MaxHeap:
  
    def __init__(self, maxsize):
          
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
  
    def parent(self, pos): 
        return pos // 2
  
    def leftChild(self, pos):
        return 2 * pos
  
    def rightChild(self, pos):
        return (2 * pos) + 1
  
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
  
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])
  
    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                if (self.Heap[self.leftChild(pos)] > 
                    self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))
  
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
  
        current = self.size
  
        while (self.Heap[current] > 
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
  
    def Printo(self):         
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + 
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))
  
    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
          
        return popped

if __name__ == '__main__':
    fileIn = open("inputPS9.txt","r")
    fileIn_content = fileIn.read()
    print(fileIn_content)
    try:
        if fileIn_content != ' ':
            listInStr = fileIn_content.split()
            listMain = [int(i) for i in listInStr] #[1, 5, 3, 8, 7, 2, 6, 10, 1, 5, 8, 4, 8]
            masterList = []
            a = 0
            c = 0
            print(listMain)

            # numberOfTestCases = listMain[0]
            # print(numberOfTestCases)
            # if numberOfTestCases>=1:
            #     while numberOfTestCases != 0:
            #         b=listMain[a+1]
            #         masterList[c] = listMain[b:((b*2)+1)]
            #         print(masterList)
            #         a=len(masterList[c])
            #         c+=1
            #         numberOfTestCases-=1
            # else:
            #     print("Test case count cannot be less than 1")

            # N = listMain[1] # total number of sweets
            # print(N)
            # M = listMain[2] # dilvery cost
            # print(M)
            # cost_of_sweets = listMain[3:3+N] #[8, 7, 2, 6, 10]

                
            # minimum_delivery_charge = listMain[3+N:] #[1, 5, 8, 4, 8]

            # i=0
            # maxHeap = MaxHeap(15)
            # while i < len(cost_of_sweets):
            #     maxHeap.insert(cost_of_sweets[i])
            #     maxHeap.Printo()
            #     i+=1

            # print("The Max val is " + str(maxHeap.extractMax()))
        else:
            print("File has no Data")
    except Exception as e:
        print("Error Message is :" + e)
    finally:
        fileIn.close()



