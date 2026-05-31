from stack import Stack

class bracketsCheck:
    def __init__(self):
        self.list = Stack()
    
    def checkBracket(self, sequence):
        for bracket in sequence:
            if bracket in ['(', '{', '[']:
                self.list.push(bracket)
            elif bracket in [')', '}', ']']:
                if self.list.isEmpty():
                    return False
                
                latest_bracket = self.list.pop()

                if (bracket == ')' and latest_bracket != '(') or (bracket == '}' and latest_bracket != '{') or (bracket == ']' and latest_bracket != '['):
                    return False
                
        return self.list.isEmpty()
    
checker = bracketsCheck()
userInput = input("Enter a sequence of brackets: ")

if checker.checkBracket(userInput):
    print("The sequence of brackets is valid.")
else:
    print("The sequence of brackets is invalid.")