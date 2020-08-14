
""""
FIFO
"""

class Stack():

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)
        pass

    def pop(self):
        self.item.pop()
        pass

    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):

        if self.item == []:
            return True
        else:
            return False
    def display(self):
        l = stack.size()
        if l!= 0:
            l -= 1
            while l>=0:
                print(self.item[l],end="")
                l -= 1

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    print("")
    print(stack.size())
    print(stack.peek())


    stack.pop()
    print(stack.size())
    print(stack.peek())

    print(stack.isempty())









