#!/usr/bin/python3


def nqueens(n: int) -> list:
    """
    >>> print(nqueens(4))
    [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
    """
    result = []
    col_set = set()
    neg_diagonal = set()
    pos_diagonal = set()
    board = [["."] * n for i in range(n)]

    def back(row_no):
        if row_no == n:
            """
            current board is a valid solution,
            format it and add it to result
            """
            valid_board = ["".join(row) for row in board]
            result.append(valid_board)
            return
        for col_no in range(n):
            if col_no in col_set or (row_no + col_no) in pos_diagonal or (row_no - col_no) in neg_diagonal:
                """
                if the position has already been used, skip it
                otherwise place a queen there and mark the position
                as used
                """
                continue
            board[row_no][col_no] = "Q"
            col_set.add(col_no)
            pos_diagonal.add(row_no + col_no)
            neg_diagonal.add(row_no - col_no)
            back(row_no + 1)
            #clean the board and sets to check for other solutions
            board[row_no][col_no] = "."
            col_set.remove(col_no)
            pos_diagonal.remove(row_no + col_no)
            neg_diagonal.remove(row_no - col_no)
        #call the func with the first row
    back(0)
    return result
if __name__ == "__main__":
    import doctest
    doctest.testmod()
