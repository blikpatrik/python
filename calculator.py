value=eval(input('How many?'))
function=input('How combine? (*/+-)')
unit=eval(input('How much?'))
while(type(value)==int and 
type(unit)==int):
  if(function=='+'):
    result=value+unit
  elif(function=='-'):
    result=value-unit
  elif(function=='*'):
    result=value*unit
  elif(function=='/'):
    result=value/unit
  print(result)
