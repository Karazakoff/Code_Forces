
word = input()
n = 0
i = 0
t = 0
e = 0
for number in word:
  if number == 'n':
    n = n + 1
  if number == 'i':
    i = i + 1
  if number == 't':
    t = t + 1
  if number == 'e':
    e = e + 1
e = e // 3
sum = 0
if n >= 5:
  while n >= 3:
    sum += 1
    n = n - 2
  print(min(sum,i,t,e))
else:
  if n < 3:
    print(min(0,i,t,e))
  else:
    print(min(1,i,t,e))
