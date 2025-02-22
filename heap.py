class Heap:
    def __init__(self):
        self.elems = []

    @staticmethod
    def left_child(idx):
        return 2 * idx + 1

    @staticmethod
    def right_child(idx):
        return 2 * idx + 2

    @staticmethod
    def parent(idx):
        return (idx-1) // 2

    def __str__(self):
        return str(self.elems)

    def has_a_child(self, idx):
        return len(self.elems) > 2 * idx + 1

    def has_two_children(self, idx):
        return len(self.elems) > 2 * idx + 2

    def higher_priority(self, a, b):
        return self.elems[a] > self.elems[b]

    def is_empty(self):
        return len(self.elems) == 0

    def swap(self,a,b):
        temp = self.elems[b]
        self.elems[b] = self.elems[a]
        self.elems[a] = temp

    def peek(self):
        return self.elems[0]

    def pop(self):
        top = self.elems[0]
        last = self.elems[len(self.elems)-1]
        self.elems.pop(len(self.elems) - 1)
        if self.is_empty():
            return top
        self.elems[0] = last
        self.heapify_down(0)
        return top

    def push(self, item):
        self.elems.append(item)
        self.heapify_up(len(self.elems)-1)

    def heapify_down(self, idx):
        if not self.has_a_child(idx):
            return

        lchild = Heap.left_child(idx)
        rchild = Heap.right_child(idx)

        if not self.has_two_children(idx):
            if self.higher_priority(idx, lchild):
                return
            else:
                self.swap(idx, lchild)
                self.heapify_down(lchild)
        else:
            if (self.higher_priority(idx, lchild) and
                self.higher_priority(idx, rchild)):
                return
            else:
                if self.higher_priority(rchild, lchild):
                    self.swap(idx, rchild)
                    self.heapify_down(rchild)
                else:
                    self.swap(idx, lchild)
                    self.heapify_down(lchild)

    def heapify_up(self, idx):
        if idx == 0:
            return
        parent = Heap.parent(idx)
        if self.higher_priority(idx, parent):
            self.swap(idx, parent)
            self.heapify_up(parent)


def main():
    h = Heap()
    a = [5,1,10,2,3,5,9,2]
    for i in a:
        h.push(i)

    for i in range(8):
        print(h.pop())
        print(h)



main()