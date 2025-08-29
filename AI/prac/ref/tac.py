def dominance(arr):
    x_count = arr.count('x')
    o_count = arr.count('o')

    if x_count == 3:
        return 100
    elif o_count == 3:
        return -100
    elif x_count > o_count:
        return x_count
    elif o_count > x_count:
        return -o_count
    else:
        return 0

def strength(board):
    rows = board
    coulmns = [[board[0][0], board[1][0], board[2][0]],
               [board[0][1], board[1][1], board[2][1]],
               [board[0][2], board[1][2], board[2][2]]]
    
    diagonals = [[board[0][0], board[1][1], board[2][2]],
                 [board[0][2], board[1][2], board[2][0]]]
    
    print("row dominanace:")
    for i, row in enumerate(rows):
        dom = dominance(row)
        if dom == 100:
            print(f"row{i+1} is dominated by 'x'")
        elif dom == -100:
            print(f"row {i+1} is dominated by 'o'" )
        else:
            print(f"row {i+1} not fully dominated by (dominance: {dom})" )
    
    print("\ncoulmn domninance:")
    for i, col in enumerate(coulmns):
        dom = dominance(coulmns)
        if dom == 100:
            print(f"coulmn {i+1} is dominated by 'x'" )
        elif dom == -100:
            print(f"coulmn {i+1} is dominated by 'o'" )
        else:
            print(f"coulmn {i+1} not fully dominated by (dominance: {dom})" )

    print("\ndiagonal dominance")
    for i, diag in enumerate(diagonals):
        dom = dominance(diag)
        if dom == 100:
            print(f"diagonal {i+1} is dominated by 'x'" ) 
        elif dom == -100:
            print(f"diagonal {i+1} is dominated by 'o'" )  
        else:
            print(f"diagonal {i+1} not fully dominated by (dominance: {dom})" )  

    total_x_dominance = 0
    total_o_dominance = 0

    for line in rows + coulmns + diagonals:
        dom = dominance(line)
        if dom > 0:
            total_x_dominance += dom  
        elif dom < 0:
            total_x_dominance -= dom
    return total_x_dominance - total_o_dominance

board = [['x', 'b', 'b'],
         ['b', 'x', 'b'],
         ['o', 'b', 'x']]
     
print("\nboard is dominating by the factor of, ",strength(board))


   