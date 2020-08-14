

class Queue():
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        if self.item:
            self.item.pop()
        else:
            return None

    def peek(self):
        if self.item:
            return self.item[-1]

    def isempty(self):
        if self.item == []:
            return True
        else:
            return False

    def size(self):
        return len(self.item)

    def display(self):
        l = queue.size()
        if l != 0:
            l -= 1
            while l >= 0:
                print(self.item[l], end="")
                l -= 1

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(item=1)
    queue.enqueue(item=2)
    queue.enqueue(item=3)

    queue.display()
    print("")
    print("Size\t{}".format(queue.size()))
    print("Peek\t{}".format(queue.peek()))

    queue.dequeue()
    print("Size\t{}".format(queue.size()))
    print("Peek\t{}".format(queue.peek()))




