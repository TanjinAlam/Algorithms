class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


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
                                    # Here self.head is also None at the beginning
        self.head = new_node        # Making the current node as the root node
        self.size += 1

    def insert_at_end(self,data):


        if self.head == None:

            new_node = node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        itr = self.head
        cnt = 0
        while itr:

            cnt += 1

            if self.get_length() == cnt:

                new_node = node(data)
                new_node.next = itr.next
                itr.next = new_node
                self.size += 1
                break
            else:

                itr = itr.next






    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:

                new_node = node(data)
                new_node.next = itr.next
                itr.next = new_node
                self.size += 1
                break

            itr = itr.next
            count += 1

    def get_length(self):
        return self.size

    def search_element(self,data):
        cnt = 0
        itr = self.head
        while itr:
            cnt += 1
            f = 0
            if(itr.data==data):
                print(str(data)+str(" FOUNDED AT INDEX ")+str(cnt-1))
                f = 1
                break
            else:
                itr = itr.next
        if(f==0):
            print(str(data)+str(" IS NOT PRESENT IN THE LINKLIST"))

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.size -= 1
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                self.size -= 1
                break

            itr = itr.next
            count +=1

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def sort(self):
        if self.size > 1:
            newlist = [];
            current = self.head
            newlist.append(self.head)
            while current.next:
                current = current.next
                newlist.append(current)
            newlist = sorted(newlist, key=lambda node: node.data, reverse=False)
            newll = LinkedList();
            for node in newlist:
                newll.insert_at_end(node.data)
            newll.print()
        return self

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.print()
    print(ll.get_length())

    ll.insert_at(3, 4)
    ll.print()
    ll.search_element(1)
    ll.print()
    ll.insert_at_end(5)
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.swap_nodes(2,4)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.insert_at_end(8)
    ll.print()
    ll.sort()
    ll.print()
    ll.insert_at_end(9)
    ll.print()
    print(ll.get_length())
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