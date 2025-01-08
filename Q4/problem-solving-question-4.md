---
title: Problem Solving Question
tags: ['tic-tac-toe', 'file-handling','tsv','logic-building','loops']
---

# Problem Statement
## Tic-Tac-Toe Winner
    Two players `A` and `B` wanted to decide who is cooking tonight's dinner.So they played 80 tic-tac-toe games to decide it. 
    You are given a file with records of past games, now it is time to decide the winner. Consider the rules below.

        > X was chosen by player A
        > O was chosen by player B
        > - represents an empty cell
        
    the file `tic-tac-toe.tsv` has a record of 80 games played between A and B.The format is tab seperated values.
    Each row in the file represents a tic-tac-toe board.
    

    find the overall winner and the number of times he/she has won, return this in a tuple.if there is a draw between players return both the players and their corresponding win count.

**example**

```XXXOOX---  represents a board```   
``` 
    |X X X|
    |O O X|
    |- - -|
```                          
# Solution
```python test.py  -r 'python test.py'

<template>
#implement your code below
<sol>
    import csv

    def read_tic_tac_toe_file(filename):
    
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='\t')  
            games = [row for row in reader]  

        return games

    def read_boards():
        boards = read_tic_tac_toe_file('tic-tac-toe.tsv')
        return boards
            

    def check_winner(board):
        win_conditions = [
        
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        
        (0, 4, 8), (2, 4, 6)]
    
        for a, b, c in win_conditions:
            if board[a] == board[b] == board[c] and board[a] in ['X', 'O']:
                return board[a]  # Return the winner ('X' or 'O')
    
        return None  
    def main():
        winner_count = {'A':0,'B':0}
        boards = read_boards()
        for board in boards:
            winner  = check_winner(board)
            if winner=='X':
                winner_count['A']+=1
            elif winner=='O':
                winner_count['B']+=1
            else
                continue
        #decide winner
        if winner_count['A']>winner_count['B']:
            return ('A',winner_count['A'])
        elif winner_count['A']<winner_count['B']:
            return ('B',winner_count['B'])
        else:
            return ('A','B',winner_count['A'])
    
    # main driver code
    main()

</sol>
</template>


```

# Private Test Cases

## Input 1

```
X	X	X	O	O	X	-	-	-
O	O	O	X	X	O	X	-	-
X	O	X	O	O	X	X	X	O
X	X	X	O	O	X	-	-	X
O	X	O	X	X	X	-	-	O
X	O	X	O	X	-	X	-	X
X	X	O	X	O	X	-	-	O
O	X	O	X	X	X	X	X	O
X	X	X	O	O	X	-	X	X
X	X	X	O	X	-	X	X	O
O	O	X	O	X	X	X	X	X
X	O	O	X	X	X	-	-	X
X	X	O	X	O	X	X	-	X
X	X	X	O	O	X	-	-	O
O	X	X	X	X	O	-	-	X
X	X	X	X	O	X	-	X	X
X	O	O	X	X	O	X	-	O
X	X	X	X	O	X	-	-	X
X	X	O	X	X	X	-	-	X
O	X	X	X	O	X	X	X	X
X	X	O	O	X	X	-	-	X
O	X	X	X	O	X	-	X	O
O	X	X	X	X	X	-	-	X
X	X	X	O	X	-	-	O
O	X	O	X	X	X	-	X	X
X	X	O	O	X	O	X	X	X
O	X	X	X	O	X	-	-	X
X	X	X	X	O	X	-	-	X
O	X	O	X	O	X	X	X	X
X	X	O	X	X	O	X	X	X
X	X	X	X	X	O	X	-	X
X	O	X	X	X	X	-	-	X
O	X	X	O	X	X	-	-	X
X	X	X	X	O	X	X	O	X
O	X	X	O	X	O	X	X	O
X	X	X	X	X	O	X	X	X
O	O	X	X	X	O	X	-	X
X	X	O	X	X	O	X	-	O
X	X	X	X	O	X	-	-	X
O	O	X	O	X	X	X	X	X
X	X	X	X	X	X	X	O	X
X	X	X	O	O	X	-	X	O
X	O	X	X	X	O	X	-	X
X	X	X	X	O	X	X	-	X
O	X	X	X	X	X	X	X	O
O	X	O	X	X	O	X	-	X
X	O	X	O	X	O	X	X	X
O	X	X	X	X	O	X	X	O
X	X	O	X	X	O	X	O	X
X	X	X	X	X	X	X	X	O
O	X	O	X	O	X	O	-	X
X	X	O	X	X	X	X	O	X
O	O	X	X	X	X	X	X	O
X	X	X	O	X	O	X	X	X
X	X	X	X	O	X	X	X	X
O	X	X	X	O	X	X	X	X
X	X	X	X	X	X	X	X	O
X	X	X	O	O	X	-	X	X
X	X	X	X	O	O	X	-	X
O	X	X	X	X	X	X	X	X
X	X	O	X	X	O	X	X	X
X	O	X	X	X	O	X	X	O
O	X	O	X	X	X	X	X	X
X	X	X	X	O	X	X	X	X
X	X	O	X	X	X	X	X	O
X	X	X	X	O	X	X	X	X
X	X	X	X	X	X	X	X	X
X	O	X	X	X	O	X	X	O
X	X	X	X	X	X	X	X	X
X	X	X	X	X	O	X	X	X
O	X	X	X	X	X	X	X	X
X	O	X	O	X	O	X	X	X
X	X	X	X	O	X	X	O	X
O	X	O	X	O	X	X	X	X
O	X	X	X	X	X	X	O	X
X	X	O	X	X	O	X	X	X
X	X	X	X	X	O	X	X	X
O	X	O	X	O	X	X	X	X
X	X	X	X	O	X	X	X	X
O	X	X	X	X	O	X	X	X


```

## Output 1

```
(A,42)
```


