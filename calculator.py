value=input('How many?')
function=input('How combine?')
unit=input('How much?')
if(value=='l'|function=='l'|unit=='l'):
  kill
elif(function=='+'):
  result=value+unit
elif(function=='-'):
  result=value-unit
elif(function=='*'):
  result=value*unit
elif(function=='/'):
  result=value/unit
print(result)
