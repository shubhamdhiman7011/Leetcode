class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
      n=3 # Size of the Tic-Tac-Toe board

    # Initialize rows, columns, and diagonal counters
      rows = [0] * n
      cols = [0] * n
      diag1 = 0
      diag2 = 0

    # Variable to track the current player, 1 for 'A' and -1 for 'B'
      player = 1

      for move in moves:
        row, col = move

        # Update row and column counters for the current player
        rows[row] += player
        cols[col] += player

        # Update diagonal counters if the move is on a diagonal
        if row == col:
            diag1 += player
        if row + col == n - 1:
            diag2 += player

        # Check if the current player has won
        if abs(rows[row]) == n or abs(cols[col]) == n or abs(diag1) == n or abs(diag2) == n:
            return "A" if player == 1 else "B"

        # Switch player
        player *= -1

    # Check if all moves are completed and no winner, return 'Draw'
      if len(moves) == n * n:
        return "Draw"

    # If the game is still ongoing, return 'Pending'
      return "Pending"

