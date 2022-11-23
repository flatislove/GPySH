class TicTacToeBoard():
    markers=["X","O"]

    def __init__(self):
        self.field=[['-','-','-'],['-','-','-'],['-','-','-']]
        self.active=TicTacToeBoard.markers[0]
    
    def new_game():
        return TicTacToeBoard()

    def get_field(self):
        return self.field
 
    def check_field(self):
        for i in range(3):
            row,col,all='','',''
            for j in range(3):
                row+=self.field[i][j]
                col+=self.field[j][i]
            all+=row
            if row[0]==row[1]==row[2] and row[0]!="-": return row[0]
            if col[0]==col[1]==col[2] and col[0]!="-": return col[0]
        if self.field[0][0]==self.field[1][1]==self.field[2][2] and self.field[1][1]!="-": return self.field[0][0]
        if self.field[0][2]==self.field[1][1]==self.field[2][0] and self.field[1][1]!="-": return self.field[0][2]
        if '-' not in all: return "D"

    def make_move(self,row, col):
        if 0<row<4 and 0<col<4:
            if self.field[row-1][col-1]!="-":
                print(f"Клетка {row}:{col} уже занята")
                return ""
            else:
                self.field[row-1][col-1]=self.active
                self.active=TicTacToeBoard.markers[0] if self.active==TicTacToeBoard.markers[1] else TicTacToeBoard.markers[1]
                result=self.check_field()
                if result==None: 
                    print("Продолжаем играть")
                    return ""
                elif (result in 'XO'): 
                    print(f"Победил игрок {result}\nИгра уже завершена")
                    return 0
                elif result=="D": 
                    print("Ничья\nИгра уже завершена")
                    return 0
                return ""
        else: return -1

# вариант работы из требований  

# board = TicTacToeBoard()
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(board.make_move(3, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")