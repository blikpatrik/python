doors=['O']*100
skip=0
while(skip<100):
  door=0
  while(door<100):
    if doors[door]=='O':
      doors[door]='X'
    else:
      doors[door]='O'
    for missed in range(door-skip,skip):
      print(doors[missed],end='')
    print(doors[door],end='')
    door=door+skip+1
  print('\n')
  skip=skip+1
print('The following doors are left open: ',end='')
for door in [door for door,open in enumerate(doors) if open=='O']:
  print(',',end='')
  print(door+1,end='')
print('\n')
