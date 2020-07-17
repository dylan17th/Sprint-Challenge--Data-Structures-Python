class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, item):
        if self.length == 0:
                self.storage.append(item)
                self.head = item
                self.tail = self.head
                self.length += 1

        elif self.length >= 1 and self.length < self.capacity:
                self.storage.append(item)
                self.tail = item
                self.length += 1

        else:
            replace_this_element = self.storage.index(self.head)
            self.storage[replace_this_element] = item
            self.tail = item
            if replace_this_element + 1 == self.capacity:
                self.head = self.storage[0]
            else:
                self.head = self.storage[replace_this_element + 1]

    def get(self):
        return self.storage
