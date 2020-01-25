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
  output = []
  '''
  We know that 'initialize' will always be the first command.
  So we initalize by building a max-heap.
  '''
  c = commands[0].split() #splitting by spaces the first command into a list
  if (c[0] == "initialize"):
    sorted_list = init(c[1:]) #initialize helper to create a sorted list
  
  '''
  Now we look at the rest of the commands in the list, 
  loop through and deal with each command.
  '''
  for i in commands[1:]:
    c = i.split()

    #pointer_right helper 
    if(c[0] == "move_pointer_right"):
      
    #pointer_left helper
    elif(c[0] == "move_pointer_left"):
      
    #insert helper
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

def pointer_right(A):
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

def initialize(A):
  #check items c[1:]
  #put into heap
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
