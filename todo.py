todo=['python game','write thesis']
print("Hi, I'm your Python assistant. How can I help?\n")
task=input("1. What's today? \n2. Remember something. \n3. Forget something. \n4. Highlight something.\n")
task=eval(task)
if(task==1):
  enumerate(todo)
if(task==2):
  todo.append(input("Sure, what's in plan? \n"))
if(task==3):
  todo.remove(input("OK, what's complete?"))
if(task==4):
  todo.mark()
