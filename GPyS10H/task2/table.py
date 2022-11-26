class Table:
    table:list

    def __init__(self,row,col):
        self.table=[]
        for i in range(row):
            self.table.append([0] * col)

    def __str__(self):
        res=''
        for row in self.table:
            res+=f'{row}\n'
        return res

    def get_value(self,row,col):
        if 0<=row<self.n_rows() and 0<=col<self.n_rows(): return self.table[row][col]
        else: return None

    def set_value(self,row,col,value):
        self.table[row][col]=value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0])
    
    def delete_row(self,row):
        new_table=[]
        for index,row_line in enumerate(self.table):
            if index!=row:
                new_table.append(row_line)
        self.table=new_table

    def delete_col(self,col):
        new_table=[]
        for column_line in self.table:
            new_table.append(column_line[0:col]+column_line[col+1:])
        self.table=new_table
    
    def add_row(self,row):
        new_table=[]
        position_correct=0
        for i in range(self.n_rows()+1):
            if i!=row:
                new_table.append(self.table[i-position_correct])
            else: 
                new_table.append([0]*self.n_cols())
                position_correct+=1
        self.table=new_table
        
    def add_column(self,col):
        new_table=[]
        for column_line in self.table:
            new_table.append(column_line[0:col]+[0]+column_line[col:])
        self.table=new_table