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
    '''
    for num in c[1:]:
        if(int(num) > first_pointer):
            pointer_list.append(int(num))
        else:
            pre_pointer.append(int(num))
    
    pre_pointer.sort()
    '''
    for num in c[1:]:
        pointer_list.append(int(num))
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
    print(get_value(pointer_list))
    
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

def insert(A, x):
    #insert new i into A
    A.append(x)
    #  Bubble Up pg 28 of course notes slightly modified
    i = len(A) - 1
    while (i > 0):
        current = A[i]
        parent = A[i//2]
        if current >= parent:
            break
        else:
            A[i] , A[i//2] = A[i//2], A[i]
            i//2
            
def get_value(A):
  #check root
  return A[0]

def initialize(pointer_list, pre_pointer):
    #build min heap
    i = floor(len(pointer_list)/2)
    pointer = poonter_list[0]
    while (i > 0):
        BubbleDown(pointer_list, i)
        i = i-1
    while(pointer != pointer_list[0]):
        pre_pointer.append(ExtractMin(pointer_list))
    
        

#return root element
def ExtractMin(A):
    temp = A[0]
    A[0] = A[len(A)-1]
    BubbleDown(A, 0)
    return temp
    
#move node in position i down as needed
def BubbleDown(A, i):
    while(i*2) <= len(A)-1:
        root = A[i]
        left_child = NULL
        right_child = NULL
        
        if (2*i+1 < len(A)-1):
            left_child = A[2*i+1]
            
        if (2*i+2<len(A)-1):
            right_child = A[2*i+2]
            
            
        if (root <= left_child and root <= right_child):
            break
            
        elif (left_child <= right_child):
            A[i], A[i*2] = A[2*i], A[i]
            i = 2*i
            
        else:
            A[i], A[i*2 + 1] = A[2*i + 1], A[i]
            i = 2*i + 1
        
#move node in position i up as needed
def BubbleUp(A, i):
    
    
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
