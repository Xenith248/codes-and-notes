def dominance(arr, player):
    opponent = 'o' if player == 'x' else 'x'
    

    if opponent in arr:
        return 0
    
   
    if arr[0] == player and arr[1] == player and arr[2] == player:
        return 3
    elif (arr[0] == player and arr[1] == player) or (arr[1] == player and arr[2] == player) or (arr[0] == player and arr[2] == player):
        return 2
    elif player in arr:
        return 1
    else:
        return 0

def dom(arr):
   
    if arr[0] == arr[1] == arr[2] == 'x':
        return 100, 0
    if arr[0] == arr[1] == arr[2] == 'o':
        return 0, 100
    
    dom_x = dominance(arr, 'x')
    dom_o = dominance(arr, 'o')
    
    return dom_x, dom_o

def strength(board):
    total_dominance_x = 0
    total_dominance_o = 0


    for i in range(3):
        dom_x, dom_o = dom(board[i])
        total_dominance_x += dom_x
        total_dominance_o += dom_o

 
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        dom_x, dom_o = dom(col)
        total_dominance_x += dom_x
        total_dominance_o += dom_o

   
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    
    dom_x, dom_o = dom(diag1)
    total_dominance_x += dom_x
    total_dominance_o += dom_o
    
    dom_x, dom_o = dom(diag2)
    total_dominance_x += dom_x
    total_dominance_o += dom_o

  
    final_strength_x = total_dominance_x - total_dominance_o
    final_strength_o = total_dominance_o - total_dominance_x

    return final_strength_x, final_strength_o


board = [
    ['x', 'o', 'x'],
    ['x', 'x', 'b'],
    ['o', 'o', 'o']
]
strength_x, strength_o = strength(board)
if (strength_o >=100):
    print(f"Strength of 'o': {strength_o}")
elif (strength_x >= 100):
    print(f"Strength of 'x': {strength_x}")
else:
     print(f"Strength of 'o': {strength_o}")
     print(f"Strength of 'x': {strength_x}")