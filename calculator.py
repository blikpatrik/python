value=0
function='+'
unit=0
print('Python calculator. Enter a letter to close.')
while True:
  try:
    value=eval(input('How many? '))
  except:
    break
  function=input('How combine? (*/+-) ')
  try:
    unit=eval(input('How much? '))
  except:
    break

  if(function=='+'):
    value=value+unit
  elif(function=='-'):
    value=value-unit
  elif(function=='*'):
    value=value*unit
  elif(function=='/'):
    value=value/unit
  print(value)
