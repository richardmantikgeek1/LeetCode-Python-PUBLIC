class Solution:
    def numRookCaptures(self, board):
        R_coord = None
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if (board[i][j] == 'R'):
                    R_coord = (i,j)

        count_pawns_to_be_captured = 0
        for i in range(R_coord[0]-1, -1, -1):
            if (board[i][R_coord[1]] == 'B'):
                break
            if (board[i][R_coord[1]] == 'p'):
                count_pawns_to_be_captured += 1
                break
        for i in range(R_coord[0]+1, len(board)):
            if (board[i][R_coord[1]] == 'B'):
                break
            if (board[i][R_coord[1]] == 'p'):
                count_pawns_to_be_captured += 1
                break
        for j in range(R_coord[1]-1,-1,-1):
            if (board[R_coord[0]][j] == 'B'):
                break
            if (board[R_coord[0]][j] == 'p'):
                count_pawns_to_be_captured += 1
                break
        for j in range(R_coord[1]+1,len(board[0])):
            if (board[R_coord[0]][j] == 'B'):
                break
            if (board[R_coord[0]][j] == 'p'):
                count_pawns_to_be_captured += 1
                break
            
        return count_pawns_to_be_captured