# THE WATER PROBLEM
# Author: Tyler Hugenberg
# how do you pythong?


def list_max(hist):
  return reduce((lambda x, y: max(x, y)), hist, hist[0])

# assume list is 2 or longer
def list_two_maxes(hist):
  m1 = max(hist[0], hist[1])
  m2 = min(hist[0], hist[1])

  for i in range(2, len(hist)):
      if hist[i] > m2:
        m2 = hist[i]
        if m2 > m1:
          m2, m1 = m1, m2

  return m1, m2

# assume list is 2 or longer
def list_two_maxes_indices(hist):
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

  return i1, i2

def list_min(hist):
  return reduce((lambda x, y: min(x, y)), hist, hist[0])

def list_perfect_valley(hist):
  previous = hist[1]
  descending = False
  if previous > hist[0]:
    descending = True
    
  timesSwitched = 0
  for i in range(2, len(hist)):
    value = hist[i]
    if value > previous:
      if descending == True:
        timesSwitched = timesSwitched + 1
      descending = False

    if value < previous:
      if descending == False:
        timesSwitched = timesSwitched + 1
      descending = True

    previous = value

    return timesSwitched < 2

def volume_to_second_tallest(hist):
  volume = 0

  #print "list for second to tallest = ", hist

  max1, max2 = list_two_maxes(hist)
  maxIndex1, maxIndex2 = list_two_maxes_indices(hist)

  lowerIndex = min(maxIndex1, maxIndex2)
  higherIndex = max(maxIndex1, maxIndex2)

  for i in range(lowerIndex+1, higherIndex):
    value = hist[i]
    #print "vol = max2: ", max2, " - value: ", value
    volume = volume + max2 - value

  return volume

def determine_volume(hist):
  print "determine_volume hist: ", hist

  if len(hist) <= 2:
    return 0
  elif len(hist) == 3:
    # bowl shape?
    middle = hist[1]
    if middle < hist[0] and middle < hist[2]:
      m1, m2 = list_two_maxes(hist)
      return m2 - middle
    else:
      return 0
    
  elif len(hist) > 3:
    # find max and divide / conquer
    maxIndex1, maxIndex2 = list_two_maxes_indices(hist)

    # if bounds of list are the max indices, just calculate.
    if list_perfect_valley:
      return volume_to_second_tallest(hist)
    else: # otherwise divide
      tallest = list_max(hist)
      tallestIndex = hist.index(tallest)

      startList = hist[:tallestIndex + 1]
      if startList == hist:
        startList = hist[:tallestIndex]

      endList = hist[tallestIndex - 1:]
      if endList == hist:
        endList = hist[tallestIndex:]

      #print "startlist: ", startList
      #print "endList: ", endList
      return determine_volume(startList) + determine_volume(endList)

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


#test_pyramid()
#test_inverse_pyramid()
#test_something()
test_negatives()
#test_updown()

