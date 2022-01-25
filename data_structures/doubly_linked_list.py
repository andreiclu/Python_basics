class DoublyLinkedElement:
    def __init__(self, _data, _next=None, _prev = None):
        self.data = _data
        self.next = _next
        self.prev = _prev

    def __str__(self):
        prev_str = f'<->' if self.prev else ""
        next_str = f'{self.next}' if self.next else ""
        return f'{prev_str} {self.data} {next_str} '

class DoublyLinkedList:
    def __init__(self):
        self.__first = None

    def get_last_element(self):
        current_element = self.__first
        while current_element.next is not None:
            current_element = current_element.next
        return current_element

    def append(self, data):
        new_element = DoublyLinkedElement(data)
        if self.__first is None:
            new_element.prev = None
            self.__first = new_element
        else:
            last_elem = self.get_last_element()
            last_elem.next = new_element
            new_element.prev = last_elem




    def __len__(self):
        if self.__first is None:
            return 0
        current_element = self.__first
        cnt = 1
        while current_element.next is not None:
            current_element = current_element.next
            cnt += 1
        return cnt


    def delete_element(self, value): #== data, folosim value sa nu se confunde cu celalalt data din clasa mama
        if self.__first is None:
            print("There's nothing to delete in the list!")
            return
        if self.__first.next is None:
            if self.__first.data == value:
                self.__first = None
            else:
                print("Item not found")
            return
        if self.__first == value:
            self.__first = self.__first.next
            self.__first.prev = None
            return

        first = self.__first
        while first.next is not None:
            if first.data == value:
                break
            first = first.next
        if first.next is not None:
            first.prev.next = first.next
            first.next.prev = first.prev
        else:
            if first.data == value:
                first.prev.next = None
            else:
                print("Element not found")

    def extend(self, new_linked_list):
        last_element = self.get_last_element()
        new_first_elem = new_linked_list.get_first_element()
        last_element.next = new_first_elem
        new_first_elem.prev = last_element



    def get_first_element(self):
        return self.__first


    def __str__(self):
        return str(self.__first)

ddlist = DoublyLinkedList()
ddlist.append(10)
ddlist.append(20)
ddlist.append(30)
ddlist.append(40)
print(ddlist)
ddlist.delete_element(30)
print(ddlist)


new_list = DoublyLinkedList()
new_list.append(50)
new_list.append(60)

ddlist.extend(new_list)
print(ddlist)
ddlist.delete_element(80)
print(ddlist)
