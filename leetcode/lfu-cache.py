class Node:
    def __init__(self, key, val):
        self.key, self.val, self.freq = key, val, 1
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def removeLast(self):
        if self.head.next == self.tail:
            return None
        last = self.tail.prev
        self.removeNode(last)
        return last
    
    def isEmpty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size, self.minFreq, self.keyToNode, self.freqToDLL = 0, 0, {}, defaultdict(DoublyLinkedList)

    def _update(self, node):
        freq = node.freq
        self.freqToDLL[freq].removeNode(node)
        if freq == self.minFreq and self.freqToDLL[freq].isEmpty():
            self.minFreq += 1
        node.freq += 1
        self.freqToDLL[node.freq].addFront(node)

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            self._update(node)
        else:
            if self.size == self.cap:
                lfuList = self.freqToDLL[self.minFreq]
                toRemove = lfuList.removeLast()
                del self.keyToNode[toRemove.key]
                self.size -= 1
            newNode = Node(key, value)
            self.keyToNode[key] = newNode
            self.freqToDLL[1].addFront(newNode)
            self.minFreq = 1
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)