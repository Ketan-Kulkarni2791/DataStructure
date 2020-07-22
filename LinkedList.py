class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index !')

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break
            counter += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index !')

        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        counter = 0
        while itr:
            if counter == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            counter += 1

    def data_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_values(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(55)
    ll.insert_at_end(85)
    ll.insert_values(['ITC', 'HDFC Bank', 'Reliance', 'Ruchi Soya', 'MGL'])
    ll.print()
    length = ll.get_length()
    print(length)
    ll.remove_at(2)
    ll.print()
    ll.insert_at(2, 'Bandhan Bank')
    ll.print()
    ll.insert_at(0, 'Lupin')
    ll.print()
    ll.data_after_value('Ruchi Soya', 'Tata Steel')
    ll.print()
    ll.remove_by_values('HDFC Bank')
    ll.print()
