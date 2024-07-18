class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check for queens in the same row
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, col=0):
        if col >= self.n:
            solution = []
            for row in range(self.n):
                solution.append(self.board[row][:])
            self.solutions.append(solution)
            return True
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                if self.solve(col + 1):
                    return True  # Only return if one solution is found
                self.board[i][col] = 0
        return False

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()


def main():
    n = 8  # Change n to the desired board size
    n_queens = NQueens(n)
    n_queens.solve()
    print("Solutions for", n, "queens:")
    n_queens.print_solutions()


if __name__ == "__main__":
    main()
