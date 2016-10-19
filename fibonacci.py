print('fibonacci sequence: ') 
length=int(input('how long should i count? '))
rank=1
penultimate=0
print(str(rank)+'.'+' '*19+str(penultimate))
ultimate=1
rank=rank+1
print(str(rank)+'.'+' '*19+str(ultimate))
for length in range(0,length):
  current=penultimate+ultimate
  rank=rank+1
  print(str(rank)+'.'+' '*(21-len(str(rank))-len(str(current)))+str(current))
  penultimate=ultimate
  ultimate=current
