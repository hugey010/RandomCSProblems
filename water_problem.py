# THE WATER PROBLEM
# Author: Tyler Hugenberg
# how do you pythong?

# gets the max element in a list, list size > 0
def list_max(hist):
  return reduce((lambda x, y: max(x, y)), hist, hist[0])

# gets the min element in a list
def list_min(hist):
  return reduce((lambda x, y: min(x, y)), hist, hist[0])

# assume list is 2 or longer
def list_two_unique_maxes(hist):
  m1 = max(hist[0], hist[1])
  m2 = min(hist[0], hist[1])

  for i in range(2, len(hist)):
      if hist[i] > m2:
        m2 = hist[i]
        if m2 > m1:
          m2, m1 = m1, m2

  return m1, m2

# returns unique max number indices of list, (lowerMaxIndex, higherMaxIndex), list size > 1
def list_two_unique_max_indices(hist):
  i1 = 0
  i2 = 1
  m1 = hist[i1]
  m2 = hist[i2]
  if hist[i2] > m1:
    m1, m2 = hist[i2], m1
    i1, i2 = i2, i1

  for i in range(2, len(hist)):
      if hist[i] > m2:
        m2 = hist[i]
        i2 = i
        if m2 > m1:
          m2, m1 = m1, m2
          i1, i2 = i2, i1

  minIndex = min(i1, i2)
  maxIndex = max(i1, i2)
  return minIndex, maxIndex

# boolean, true if index 0 and last index are relative maximums
def list_perfect_valley(hist):
  m1, m2 = list_two_unique_max_indices(hist)
  if (m1 == 0 and m2 == len(hist)-1) or (m2 == 0 and m1 == len(hist)-1):
    return True
  return False

# finds the volume of relative maximum ended histograms
def volume_to_second_tallest(hist):
  max1, max2 = list_two_unique_maxes(hist)
  maxIndex1, maxIndex2 = list_two_unique_max_indices(hist)

  volume = 0
  for i in range(maxIndex1+1, maxIndex2):
    value = hist[i]
    volume = volume + max2 - value

  return volume

# returns the volume the historgram reprented by the argument: a being list of numbers
# if water were to be poured on top of it
def volume(hist):
  if len(hist) <= 2:
    return 0
  else: # if bounds of list are the max indices, just calculate.
    if list_perfect_valley(hist):
      return volume_to_second_tallest(hist)

    else: # divide & conquer
      maxIndex1, maxIndex2 = list_two_unique_max_indices(hist)

      startList = hist[0:maxIndex1+1]
      middleList = hist[maxIndex1:maxIndex2+1]
      endList = hist[maxIndex2: len(hist)]

      return volume(startList) + volume(middleList)  + volume(endList)

# TESTS

def test_pyramid():
  histo = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2]
  shouldbe = 0
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

def test_inverse_pyramid():
  histo = [10, 3, 2, 1, 0, 5, 9, 10]
  shouldbe = 40
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

def test_something():
  histo = [1, 3, 4, 2, 4, 5, 3, 2, 1, 4]
  shouldbe = 8
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

def test_negatives():
  histo = [1, -5, -3, 1, 3, -2, 6, 2, 1, -3]
  shouldbe = 15
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5]
  shouldbe = 10
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)


def test_holes():
  histo = [10, 9, 8, 8, 9, 8, 9, 8, 10, 4, 3, 3]
  shouldbe = 11
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [-1, -2, -3, -4, -2, -3, -4, -5, -1, -2, -3, -3]
  shouldbe = 16
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [0, 1, 2, 3, 0, -500, -1000, -1000, 0, 3, -10000, -2000000]
  shouldbe = 2500 + 3 + 3 + 3 + 3 + 3
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

def test_updown():
  histo = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3]
  shouldbe = 18
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

def test_base():
  histo = []
  shouldbe = 0
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [10]
  shouldbe = 0
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [-2, 5]
  shouldbe = 0
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [4, 1, 0]
  shouldbe = 0
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [5, -5, 5]
  shouldbe = 10
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

  histo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  shouldbe = 0
  assert shouldbe == volume(histo)
  print "For histogram: ", histo, "Actual Volume: ", shouldbe, "Calculated: ", volume(histo)

def test_1():
  histo = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
  shouldbe = 23

  print "List: ", histo, " shouldbe: ", shouldbe
  print "Calculated Water Volume: = ", volume(histo)

test_pyramid()
test_inverse_pyramid()
test_something()
test_negatives()
test_updown()
test_base()
test_holes()
test_1()
