def getFib(position):
  if position == 0:
       return 0
  elif position == 1:
      return 1
  x = []
  first = 0
  second = 1
  next = first + second
  x.append(first)
  x.append(second)
  for i in range(2,position):
    first = second
    second = next
    next = first+second
    x.append(second)
  return second,x

x,y = getFib(9)
print(x)
print(y)