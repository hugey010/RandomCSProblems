import sys

count = int(sys.argv[1]);
print "Recursive Fib: ", count

def fib(x):
  if (x == 0 or x == 1):
    return 1
  else:
    return fib(x - 2) + fib(x - 1)


result = fib(count)

print "Fib of ", count, " is ", result
