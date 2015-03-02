import sys

count = int(sys.argv[1]);

def it_fib(x):
  a, b = 0, 1
  for i in range(0, x):
    a, b = b, a + b
  return a

def rec_fib(x):
  if (x == 0):
    return 0
  if (x == 1):
    return 1;
  else:
    return rec_fib(x - 2) + rec_fib(x - 1)

print "Rec Fib of ", count, " is ", rec_fib(count)
print "Iter Fib of ", count, " is ", it_fib(count)
