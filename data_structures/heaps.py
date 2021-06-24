class Heap:
    def __init__(self):
        # Stores heap items (item, item_value).
        self.arr = []
        # Stores the position of each item in the array.
        self.pos_map = {}
        # Stores the current size of heap.
        self.size = 0

    def _left_child(self,index):
        """Return left child index of the given index else None."""
        left = (index * 2) + 1
        return left if 0 <= left < self.size else None

    def _right_child(self, index):
        """Return right child index of the given index else None."""
        right = (index * 2) + 2
        return right if 0 <= right < self.size else None

    def _parent(self, index):
        """Return parent index of the given index else None."""
        return (index - 1) // 2 if index > 0 else None

    def _swap(self, i, j):
        """Swap the item at index i with item at index j."""
        # Update the pos map with the correct index
        self.pos_map[self.arr[i][0]], self.pos_map[self.arr[j][0]] = (
            self.pos_map[self.arr[j][0]],
            self.pos_map[self.arr[i][0]],
        )
        # Swap the items in the list
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        while parent_index is not None and self.arr[parent_index][1] > self.arr[index][1]:
            self._swap(index, parent_index)
            index, parent_index = parent_index, self._parent(parent_index)

    def _heapify_down(self, index):
        while self._left_child(index):
            # Get index for smallest of two child
            small_child_index = left_child_index = self._left_child(index)
            right_child_index = self._right_child(index)
            if right_child_index is not None and self.arr[left_child_index][1] > self.arr[right_child_index][1]:
                small_child_index = right_child_index

            # Compare parent with smallest of child
            if self.arr[index][1] < self.arr[small_child_index][1]:
                break
            else:
                self._swap(index, small_child_index)

            # Update index to the swapped postion
            index = small_child_index

    def insert(self, item, item_value):
        if len(self.arr) == self.size:
            self.arr.append([item, item_value])
        else:
            self.arr[self.size] = [item, item_value]
        self.pos_map[item] = self.size
        self.size += 1
        self._heapify_up(self.size - 1)

    def delete(self, item):
        if item not in self.pos_map:
            return
        index = self.pos_map[item]
        del self.pos_map[item]
        self.arr[index] = self.arr[self.size - 1]
        self.pos_map[self.arr[self.size - 1][0]] = index
        self.size -= 1
        if self.size > 0:
            self._heapify_up(index)
            self._heapify_down(index)


    def update_item(self, item, item_value):
        if item not in self.pos_map:
            return
        index = self.pos_map[item]
        self.arr[index] = [item, item_value]
        self._heapify_up(index)
        self._heapify_down(index)

    def peek(self):
        return self.arr[0] if self.size > 0 else None

    def poll(self):
        top_item = self.peek()
        if top_item:
            self.delete(top_item[0])
        return top_item


if __name__ == "__main__":
    h = Heap()
    h.insert(8, 45)
    h.insert(9, 40)
    print(h.peek())
    h.insert(10, 30)
    print(h.peek())
    h.update_item(10, 50)
    print(h.peek())
