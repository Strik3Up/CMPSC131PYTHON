# Author: 
def f1(a):
  if (a < 0):
    b = a*-1
  elif (a > 0):
    b = a
  else:
    b = 0
  return b

def f2(n):
  yl = [0]
  for x in range(1,n):
    fn = input("Enter an integer: ")
    t1 = f1(fn)
    yl.append(t1)
  return sum(yl)  

def run():
  ans = f"answer is {f2(n)}."
  return ans

if __name__ == "__main__": 
  run()
