C=[0,11, 9, 9, 12, 12, 12, 12, 9, 9, 11]
val = {}
pattern = {}
def OPT(i):
  r = 1
  c = 40
  if(i >= len(c)):
    print("cannot be calculated with the following")
    
  if i == 0:
    val[0] = 0
    return val[0]
  if i>= 1 and i < 4:
    if not i in val:
      val[i] = (r*C[i] + OPT(i-1))
      pattern[i] = 'b'
    pattern[i] = 'a'
    return val[i]
  if i >= 4:
    val[i] = min((r*C[i] + OPT(i-1)),(c+OPT(i-4)))
    pattern[i] = 'b' if(val[i] == c+OPT(i-4)) else 'a'
      
    return val[i]

OPT(10)
for k,v in pattern.items():
  print("key: " + str(k) + " val: " + str(v))
