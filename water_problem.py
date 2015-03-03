# THE WATER PROBLEM
# Author: Tyler Hugenberg
# how do you pythong?

import sys


def list_max(hist):
  return reduce((lambda x, y: max(x, y)), hist, hist[0])

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

# assume list is 2 or longer
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

def list_min(hist):
  return reduce((lambda x, y: min(x, y)), hist, hist[0])

# perfect if ends are relative maximums
def list_perfect_valley(hist):

  m1, m2 = list_two_unique_max_indices(hist)

  if (m1 == 0 and m2 == len(hist)-1) or (m2 == 0 and m1 == len(hist)-1):
    return True
  return False

def volume_to_second_tallest(hist):

  max1, max2 = list_two_unique_maxes(hist)
  maxIndex1, maxIndex2 = list_two_unique_max_indices(hist)

  volume = 0
  for i in range(maxIndex1+1, maxIndex2):
    value = hist[i]
    volume = volume + max2 - value

  return volume

def determine_volume(hist):
  if len(hist) <= 2:
    return 0
  else:
    # if bounds of list are the max indices, just calculate.
    if list_perfect_valley(hist):
      return volume_to_second_tallest(hist)

    else: # find max and divide / conquer
      maxIndex1, maxIndex2 = list_two_unique_max_indices(hist)

      startList = hist[0:maxIndex1]
      middleList = hist[maxIndex1:maxIndex2+1]
      endList = hist[maxIndex2: len(hist)]

      return determine_volume(startList) + determine_volume(middleList)  + determine_volume(endList)

def test_pyramid():
  histo = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2]
  shouldbe = 0

  print "List: ", histo, " shouldbe: ", shouldbe
  print "Calculated Water Volume: = ", determine_volume(histo)

def test_inverse_pyramid():
  histo = [10, 3, 2, 1, 0, 5, 9, 10]
  shouldbe = 40

  print "List: ", histo, " shouldbe: ", shouldbe
  print "Calculated Water Volume: = ", determine_volume(histo)

def test_something():
  histo = [1, 3, 4, 2, 4, 5, 3, 2, 1, 4]
  shouldbe = 8

  print "List: ", histo, " shouldbe: ", shouldbe
  print "Calculated Water Volume: = ", determine_volume(histo)

def test_negatives():
  histo = [1, -5, -3, 1, 3, -2, 6, 2, 1, -3]
  shouldbe = 15

  print "List: ", histo, " shouldbe: ", shouldbe
  print "Calculated Water Volume: = ", determine_volume(histo)

def test_updown():
  histo = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3]
  shouldbe = 18

  print "List: ", histo, " shouldbe: ", shouldbe
  print "Calculated Water Volume: = ", determine_volume(histo)


test_pyramid()
test_inverse_pyramid()
test_something()
test_negatives()
test_updown()

