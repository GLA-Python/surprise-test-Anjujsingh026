def expanding(lst):
  lst1 = []
  try:
    for i in range(len(lst)):
      out = (lst[i+1])-lst[i]
      lst.append(abs(out))
  expect:
    lst.append(lst[-1])
  if sorted(lst[-1]==lst1:
            return True
  else:
            return False
lst=list(mao(int,input("Enter the numbers : ").split(",")))
print(expanding(lst))
            
            
