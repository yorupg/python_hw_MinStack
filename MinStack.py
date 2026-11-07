class MinStack:
    
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, number: int ) -> None:
        
        if len(self.stack) == 0:
            self.current_min = number
            
        if number < self.current_min:    
            self.current_min = number
      self.stack.append((self.current_min, number))
        
    def pop(self) -> None:
        
        if len(self.stack) == 0:
            raise IndexError("нельзя удалить элемент из пустого стека")
        
        if self.current_min == self.stack[-1][1]:
            if len(self.stack) > 1:
                self.current_min = self.stack[-2][0]
            else:
                self.current_min = None
            
        self.stack.pop()
        
        
    def get_min(self) -> int:
        
        if len(self.stack) == 0:
            raise IndexError("стек пуст")
        
        return self.stack[-1][0]
    
    def top(self) -> int:
        
        if len(self.stack) == 0:
            raise IndexError("стек пуст")
        
        return self.stack[-1][1]
    
stack = MinStack()

try:
    stack.get_min()
    
except IndexError as error:
    assert str(error) == "стек пуст"
    
try:
    stack.pop()
    
except IndexError as error:
    assert str(error) == "нельзя удалить элемент из пустого стека"


stack.push(-2)
stack.push(0)
stack.push(-3)

assert stack.get_min() == -3

stack.pop()

assert stack.top() == 0
assert stack.get_min() == -2