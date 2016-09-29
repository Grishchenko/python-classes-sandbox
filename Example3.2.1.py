import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["ch"])):
    def walk(self, code, acc):
        code[self.ch] = acc or "0"


def huffman_encode(s):
    h = []
    for char, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(char)))
    heapq.heapify(h)

    count = len(h)

    while len(h) > 1:
        freq_1, _count1, left = heapq.heappop(h)
        freq_2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq_1 + freq_2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[char] for char in s)
    print(len(code), len(encoded))
    for char in sorted(code):
        print("{}: {}".format(char, code[char]))
    print(encoded)

if __name__ == '__main__':
    main()