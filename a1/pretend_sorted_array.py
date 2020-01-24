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
  pass # TODO: implement this function


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
