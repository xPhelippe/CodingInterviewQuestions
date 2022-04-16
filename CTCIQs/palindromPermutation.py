str = "taca cat"

def isPalPerm(str):

  if len(str) == 0:
    return True

  str = str.lower()
  
  charFreq = {}

  oddBool = False

  for el in str:
    if el == ' ':
      continue
    
    if el in charFreq:
      charFreq[el] = charFreq[el] + 1
    else: 
      charFreq[el] = 1

  for key in charFreq.keys():
    freq = charFreq[key]
    
    if freq % 2 == 1:
      if oddBool:
        return False
      else:
        oddBool = True

  return True

print(isPalPerm(str))
