class Element(object):

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def printList(self):
        current = self.head
        print "\nList:"
        print "-------------"
        if current:
            while current.next:
                print "Value: " + str(current.value)
                current = current.next
            print "Value: " + str(current.value)
        print "-------------\n"

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        i = 1
        current = self.head
        if current:
            while i < position:
                if current.next:
                    current = current.next
                i += 1
            return current
        return None

    def insert(self, new_element, position):
        i = 1
        current = self.head
        if current:
            while i < position - 1:
                current = current.next
                i += 1
            new_element.next = current.next
            current.next = new_element
        pass


    def delete(self, value):
        current = self.head
        if current:
            if self.head.value == value:
                self.head = self.head.next
            else:
                while current.next:
                    next = current.next
                    if current.value == value:
                        current.next = next.next
                    current = current.next
        pass

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value == 3
# Should also print 3
print ll.get_position(3).value == 3

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value == 4

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value == 2
# Should print 4 now
print ll.get_position(2).value == 4
# Should print 3 now
print ll.get_position(3).value == 3
