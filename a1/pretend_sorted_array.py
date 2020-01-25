'''
CSC263 Winter 2020
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def pretend_sorted_array(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of outputs
  '''
  # TODO: implement this function
  output = []
  for i in commands:
    c = i.split()
    if (c[0] == "initialize"):
      sorted_list = init(c[1:])
      #initialize helper
      
    elif(c[0] == "move_pointer_right"):
      #pointer_right helper
    
    elif(c[0] == "move_pointer_left"):
      #pointer_left helper
      
    elif (c[0] == "insert"):
      insert(A, int(c[1]))
          
    #add pointer to output list
    #get val helper       
  return output
      
#Helper Functions
def pointer_left(A):
  #remove pointer
  #predecessor
  #find and add pointer
  #return new list
  return 0

def point_right(A):
  #remove pointer
  #sucessor
  #find and add pointer
  return 0

def insert(A, i):
  #insert new i into A
  #upadte_pointer if new element goes before pointer
  return 0
  
def get_value(A):
  #find pointer and return key
  return p

def init(A):
  #check items c[1:]
  #put into ADT
  #return datatype
  return ADT

if __name__ == '__main__':

  # some small test cases
  # Case 1
  assert [4, 4, 7, 7, 6, 7, 8, 12] == pretend_sorted_array(
    [ 'initialize 4 15 7 12',
      'move_pointer_left',
      'move_pointer_right',
      'insert 8',
      'insert 6',
      'move_pointer_right',
      'move_pointer_right', 
      'move_pointer_right',
    ])
