class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def isValidCell(i,j,board):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                return True
            else:
                return False


        def check_for_word(board,i,j,word):
            if not isValidCell(i,j,board):
                return False
            if board[i][j]=='1' or board[i][j]!=word[0]:
                return False
            if not word or (len(word)==1 and board[i][j]==word[0]):
                return True
            bp,board[i][j]=board[i][j],'1'

            if check_for_word(board,i+1,j,word[1:]):
                return True
            if check_for_word(board,i-1,j,word[1:]):
                return True
            if check_for_word(board,i,j+1,word[1:]):
                return True
            if check_for_word(board,i,j-1,word[1:]):
                return True
            board[i][j]=bp
            return False

        def find_possible(board,word):
            res=[]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==word:
                        res.append((i,j))
            return res


        if not word or len(board[0])==0 or not board[0]:
            return False

        possible_val=[]

        possible_val=find_possible(board,word[0])
        if len(possible_val)==0:
            return False
        for i,j in possible_val:
            if check_for_word(board,i,j,word):
                return True
        return False

sol=Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(sol.exist(board,"ABCB"))