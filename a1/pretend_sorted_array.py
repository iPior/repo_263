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
  pointer_list = []
  pre_pointer = []
  '''
  We know that 'initialize' will always be the first command.
  So we initalize by building a max-heap.
  '''
  c = commands[0].split() #splitting by spaces the first command into a list
  if (c[0] == "initialize"):
    first_pointer = int(c[1])
    for num in c[1:]:
        if(int(num) > first_pointer):
            pointer_list.append(int(num))
        else:
            pre_pointer.append(int(num))
    
    
    initialize(pointer_list, pre_pointer)#initialize helper to create a sorted list
  
  '''
  Now we look at the rest of the commands in the list, 
  loop through and deal with each command.
  '''
  for i in commands[1:]:
    c = i.split()

    #pointer_right helper 
    if(c[0] == "move_pointer_right"):
      pointer_right(pointer_list, pre_pointer)
      
    #pointer_left helper
    elif(c[0] == "move_pointer_left"):
      pointer_left(pointer_list, pre_pointer)
      
    #insert helper
    elif (c[0] == "insert"):
      insert(A, int(c[1]))
          
    #add pointer to output list
    output.append(get_value(pointer_list))
    print(get_value(pointer_list)
    
  print(output)
  return output
      
#Helper Functions
def pointer_left(pointer_list, pre_pointer):
    #Check pre_pointer, if empty no change to pointer
    if (len(pre_pointer) == 0):
        break
    #If not empty remove elememt at [-1] and insert into MinHeap
    new_pointer = pre_pointer.pop()
    insert(pointer_list, new_pointer)

def pointer_right(pointer_list, pre_pointer):
  #remove "root"/min element (extract min)
  root = ExtractMin(pointer_list)
  #add to pre_pointer
  pre_pointer.append(root)

def insert(A, i):
  #insert new i into A
  A.append(i)
  BubbleUp(A, len(A)-1)
  
def get_value(A):
  #check root
  return A[0]

def initialize(pointer_list, pre_pointer):
    #build min heap
    i = floor(len(pointer_list)/2)
    while (i >= 0):
        BubbleDown(pointer_list, i)
        i = i-1
#    order pre_pointer?
    j = floor(len(pre_pointer)/2)
    while (j>=0):
        BubbleDown(pre_pointer, j)
        
def ExtractMin(A):

def BubbleDown(A, i):

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

'''
BuildMaxHeap(A):
   for i ← floor(n/2) downto 1:
      BubbleDown(A, i)
'''

#def BubbleDown(heap, i):
# while i*2 <= heap.size:
#   curr_p = heap[i].priority
#   left_p = heap[2*i].priority
#   right_p = heap[2*i + 1].priority # -inf if not exist
# 
#   # heap property is satisfied
#   if curr_p >= left_pandcurr_p >= right_p:
#     break
#   # left child has higher priority
#   elif left_p >= right_p:
#     PQ[i], PQ[2*i] = PQ[2*i], PQ[i]
#     i = 2*i
# 
#   # right child has higher priority
#   else:
#     PQ[i], PQ[2*i + 1] = PQ[2*i + 1], PQ[i]
#     i = 2*i + 1
