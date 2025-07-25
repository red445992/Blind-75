class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Add two numbers represented as linked lists.
        The digits are stored in reverse order (least significant digit first).
        
        Time Complexity: O(max(m, n)) where m and n are lengths of the lists
        Space Complexity: O(max(m, n)) for the result list
        """
        dummy = ListNode(0)  # Dummy node to simplify list construction
        current = dummy
        carry = 0

        # Continue while there are digits to process or carry exists
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10  # Integer division for carry
            
            # Create new node with the digit (total % 10)
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next  # Return the actual head (skip dummy)
    
# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example usage
s = Solution()

# Create linked lists for testing
l1_arr = [2, 4, 3]  # represents 342
l2_arr = [5, 6, 4]  # represents 465
l1 = create_linked_list(l1_arr)
l2 = create_linked_list(l2_arr)

# Add the two numbers
result = s.addTwoNumbers(l1, l2)

# Print the result
print(f"Input 1: {l1_arr} (represents {l1_arr[0] + l1_arr[1]*10 + l1_arr[2]*100})")
print(f"Input 2: {l2_arr} (represents {l2_arr[0] + l2_arr[1]*10 + l2_arr[2]*100})")
print(f"Result: {print_linked_list(result)} (represents {342 + 465} = 807)")

# Test with another example
print("\n--- Another Test Case ---")
l1_arr2 = [9, 9, 9, 9, 9, 9, 9]  # represents 9999999
l2_arr2 = [9, 9, 9, 9]           # represents 9999
l1_2 = create_linked_list(l1_arr2)
l2_2 = create_linked_list(l2_arr2)

result2 = s.addTwoNumbers(l1_2, l2_2)
print(f"Input 1: {l1_arr2}")
print(f"Input 2: {l2_arr2}")
print(f"Result: {print_linked_list(result2)}")
