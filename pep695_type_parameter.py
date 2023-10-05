type Ponto = tuple[float, float]

p: Ponto = (3.4, 5.1)
t: Ponto
t = {"1.3": 5}
print(p, t)

type User = dict[str, str]
usr: User = {"fulano": "fulano@example.com"}
v: User
v = {1, False}
print(usr, v)

class Stack[T]:
    def __init__(self) -> None:
        self._elements: list[T] = []
    def push(self, element: T):
        self._elements.append(element)
    def pop(self) -> T:
        return self._elements.pop()
    def peek(self) -> T:
        return self._elements[-1]
    def isEmpty(self) -> bool:
        return len(self._elements) == 0
    def size(self) -> int:
        return len(self._elements)

intStack: Stack[int] = Stack[int]()
intStack.push(10)
intStack.push(20)
intStack.push(30)
print(intStack.isEmpty())
print(intStack.size())
print(intStack.pop())
intStack.push(3.4)
        


