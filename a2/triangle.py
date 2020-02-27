'''
CSC263 Winter 2020
Problem Set 2 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# Do NOT use Python dictionaries

def num_triangle_kinds(triangles):
  '''
  Pre: triangles is a list of 3-tuples representing triangles
  Post: return the number of kinds of triangles
  '''
  # TODO: implement this function
  L = []
  n = len(triangles) #Avg-Case: O(1)
  for t in triangles:
    i = hash(t[0], t[1], t[2], n) #Avg-Case: O(1)
    if not(i in L): #Avg-Case: O(1)
      L.append(i) #Avg-Case: O(1)
  return len(L) #Avg-Case: O(1)

def hash(x, y, z, n):
    #Multiplication Method for Universal Hashing
    a = 0.6180339887498949 #as suggested by Donald Knutch
    m = 2**32 #m big enough so that our hash functions has a slim chance of hashing to the same thing

    #Hash each side individualy
    x1= m*((x*a)%1)
    y1= m*((y*a)%1)
    z1= m*((z*a)%1)

    '''
    Return the addition of the hashed sides, so that triangles (1,2,3) and (2,2,2)
    do not have the same hash, but triangles (3,6,12) and (12,3,6) do have the same
    hash. 
    '''
    return x1+y1+z1

if __name__ == '__main__':

  # some small test cases
  # Case 1
  triangles = [(6, 12, 9), (9, 6, 12), (9, 6, 6), (6, 9, 9), (12, 9, 6)]
  assert 3 == num_triangle_kinds(triangles)
