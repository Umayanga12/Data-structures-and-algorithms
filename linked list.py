class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    #add the data to the linklist 
    def add(self, data:int) -> None:
        if self.head is None:
            self.head = node(data)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
    
    #remove the data from the linklist
    def remove(self,data) -> None :
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
    
    #search the data in the linklist
    def search(self,data) -> None:
        if self.head is None:
            return
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False


link_list = Linkedlist()
link_list.add()
link_list.add()
link_list.add()
print(link_list)
print(link_list.search())
link_list.remove()
print(link_list)


def merge_and_sort_linked_lists(list1, list2):

    # Create a dummy node for the new merged and sorted linked list.
    dummy_node = node(None)

    # Create two pointers, one for each of the two input linked lists.
    current_node1 = list1.head
    current_node2 = list2.head

    # Add the smaller node to the new merged and sorted linked list.
    # Move the pointer for the smaller node forward.
    current_node = dummy_node
    while current_node1 is not None and current_node2 is not None:
        if current_node1.data < current_node2.data:
            current_node.next = current_node1
            current_node1 = current_node1.next
        else:
            current_node.next = current_node2
            current_node2 = current_node2.next
        current_node = current_node.next

    # Add the remaining nodes from the other input linked list to the new merged and sorted linked list.
    if current_node1 is not None:
        current_node.next = current_node1
    elif current_node2 is not None:
        current_node.next = current_node2

    return dummy_node.next

# Example usage:

list1 = Linkedlist()
list1.add(1)
list1.add(3)
list1.add(5)

list2 = Linkedlist()
list2.add(2)
list2.add(4)
list2.add(6)

merged_list = merge_and_sort_linked_lists(list1, list2)

# Print the merged and sorted linked list.
current_node = merged_list
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = dummy = ListNode()
#         while list1 and list2:               
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#             cur.next = list1 if list1 else list2
            
#         return dummy.next