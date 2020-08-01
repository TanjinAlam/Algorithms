class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def insert_at_begining(self, data):
        new_node = node(data)
        new_node.next = self.head   # Connecting current node.next pointer to the immediate current node
        print(new_node.next)        # Here self.head is also None at the beginning
        self.head = new_node        # Making the current node as the root node






if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.print()

    #at the first call of ll.insert_at_beginning(1)
    #our current status of the link list will be like this
    # ll.head------- head node / root node holding data 1 and it's connect with next None pointer
    #      |
    #      |
    # +----+------+
    # | 1  | None ----> This is None because new_node.next is None at the beginning
    # +----+------+

    #This is the first senario where the next self.head is None
    #and then at the second call of ll.insert_at_beginning(2)
    #Initializing the node with data 2
    #By executing new_node = node(2)

    # +----+------+
    # | 2  | None + #note this None can be excess by new_node.next where we will
    # +----+------+ #use it connect it with the immediate next to it.

    #Then Connecting the current to the immediate next to it
    #since self.head is now holding the status of data(1) details
    #by executing second line new_node.next = self.head

    # +----+------+     +----+------+
    # | 2 | o - -------> | 1 | null | #this is null because it was null and it will always
    # +----+------+     +----+------+ #remain the last element of the link_list
    # '''

    #Finally we declear the current node as head node of the link list
    #by executing self.head = new_node

    # l.head
    #      |
    #      |
    # +----+------+     +----+------+
    # | 2 | o - -------> | 1 | null | #this is null because it was null and it will always
    # +----+------+     +----+------+ #remain the last element of the link_list