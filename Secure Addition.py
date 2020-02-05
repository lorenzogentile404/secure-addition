import random

# Fixed prime agreed on
p = 3761

# Common knowledge (2 parties agree on a value)
s = [None, None, None]

class Party:    
    
  def __init__(self, i, x): 
        self.i = i
        self.x = x
        self.r = [[None,None,None],[None,None,None],[None,None,None]]
        self.s = [None,None,None]
        
        self.r[i][0] = random.randint(0,p)
        self.r[i][1] = random.randint(0,p)
        self.r[i][2] = (x - self.r[i][0] - self.r[i][1]) % p
    
  def result(self):
    v = 0
    for i in range(0,len(s)):
      if self.s[i] is None:
        v += s[i]
      else:
        v += self.s[i]
    return(v % p)
        
# Step 1
    
print("Computing shares\n")
parties = [Party(0, 1), Party(1, 0), Party(2, 1)]

for i in range(0, 3):
  P = parties[i]
  print(str(P.x) + " = (" +  str(P.r[i][0])  + " + " + str(P.r[i][1]) + " + " + str(P.r[i][2]) + ") % " + str(p))
  print("r = " + str(P.r))
  print("\n")

# Step 2
  
print("Sending shares\n")
for i in range(0, 3):
  P_i = parties[i]
  for j in range(0, 3):
    P_j = parties[j]
    for k in range(0, 3):
        if j != k:
            # i,j,k belongs to (0,2) and j != k
            # P_i sends to P_j r[i,k]
            P_j.r[i][k] = P_i.r[i][k]    


for i in range(0, 3):
  P = parties[i]
  print("r = " + str(P.r))
  print("\n")
  
# Step 3
  
print("Computing and announce partial results\n")
for i in range(0, 3):
    P_i = parties[i]
    for l in range(0,3):
        if l != i:
          P_i.s[l] =  P_i.r[0][l] +  P_i.r[1][l] +  P_i.r[2][l]
          
          if s[l] is None or s[l] == P_i.r[0][l] +  P_i.r[1][l] +  P_i.r[2][l]:
              s[l] = P_i.r[0][l] +  P_i.r[1][l] +  P_i.r[2][l]
          else:
              print("Error")
    print("s_" + str(i) + " = "  + str(P_i.s))
    
print("Common knowledge: " + str(s) + "\n")
    
# Step 4

print("Computing result\n")
for i in range(0, 3):
    print("P_" + str(i) + " computes " +  str(parties[i].result()))
    
  

  

        
        
    