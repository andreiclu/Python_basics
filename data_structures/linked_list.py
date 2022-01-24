class LinkedElement:
    def __init__(self, _data, _next=None):
        self.data = _data  # de tip int
        self.next = _next  # de tip LinkedElement

    def __str__(self):
        next_str = f'-> {self.next}' if self.next else ""
        return f'{self.data} {next_str}'


class LinkedList:
    def __init__(self):
        self.__first = None

    def append(self, data):
        new_linked_element = LinkedElement(data)
        if self.__first is None:
            self.__first = new_linked_element
        else:
            last_element = self.get_last_element()
            last_element.next = new_linked_element

    def get_last_element(self):
        current_element = self.__first
        while current_element.next is not None:
            current_element = current_element.next

        return current_element

    def __len__(self):
        if self.__first is None:
            return 0
        current_element = self.__first
        cnt = 1
        while current_element.next is not None:
            current_element = current_element.next
            cnt += 1
        return cnt

    def __str__(self):
        return str(self.__first)

    def delete_element(self):
        self.__first = self.__first.next

    def extend(self, new_linked_list):
        last_element = self.get_last_element()
        last_element.next = new_linked_list.get_first_element()

    def get_first_element(self):
        return self.__first


my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list)

print('No of elements in my Linked list:', len(my_linked_list))

print('Deleting the first element:')
my_linked_list.delete_element()
print(my_linked_list)

new_linked_list = LinkedList()
new_linked_list.append(4)
new_linked_list.append(5)

print('Extending the first list: ')
my_linked_list.extend(new_linked_list)
print(my_linked_list)


