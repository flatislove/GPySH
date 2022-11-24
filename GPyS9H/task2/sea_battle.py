class SeaMap:
    shoot_results=["miss","hit","sink"]
    map_markers=[".","*","x"]
    messages=["Клетка уже отмечена ранее","Клетка за пределами поля"]

    def __init__(self):
        seamap = [[0]*10 for _ in range(10)]
        for i in range(10):
            for j in range(10):
                seamap[i][j] = "."
        self.seamap=seamap
    
    def shoot(self,row,col,result):
        if (0<=row<=10 and 0<=col<=10):
            if self.sell(row,col)==SeaMap.map_markers[0]:
                if result==SeaMap.shoot_results[0]: 
                    if self.sell(row,col)==SeaMap.map_markers[0]:self.seamap[row][col]=SeaMap.map_markers[1]
                    else: print(SeaMap.messages[0]) 
                elif result==SeaMap.shoot_results[1]: 
                    if self.sell(row,col)==SeaMap.map_markers[0]:self.seamap[row][col]=SeaMap.map_markers[2]
                    else: print(SeaMap.messages[0])
                elif result==SeaMap.shoot_results[2]:
                    direction=-1
                    steprow,stepcol=0,0
                    self.seamap[row][col]=SeaMap.map_markers[2]
                    for i in range(row-1,row+2):
                        for j in range(col-1,col+2):
                            if (-1<i<10 and -1<j<10) and self.sell(i,j)!=SeaMap.map_markers[2]:self.seamap[i][j]=SeaMap.map_markers[1]
                            if (-1<i<10 and -1<j<10) and self.sell(i,j)==SeaMap.map_markers[2] and (row!=i or col!=j):
                                direction=0 if row==i else 1
                        if direction==1:steprow,stepcol=1,0
                        elif direction==0:steprow,stepcol=0,1
                        if 0<=direction<=1:
                            while(self.sell(row+steprow,col+stepcol)==SeaMap.map_markers[2]):
                                for i in range(steprow+row-1,steprow+row+2):
                                    for j in range(stepcol+col-1,stepcol+col+2):
                                        if (-1<i<10 and -1<j<10) and self.sell(i,j)!=SeaMap.map_markers[2]:self.seamap[i][j]=SeaMap.map_markers[1]
                                if direction==1: steprow+=1
                                elif direction==0: stepcol+=1
                            if direction==1:steprow,stepcol=1,0
                            elif direction==0:steprow,stepcol=0,1
                            while(self.sell(row-steprow,col-stepcol)==SeaMap.map_markers[2]):
                                for i in range(row-1-steprow,row+2-steprow):
                                    for j in range(col-1-stepcol,col+2-stepcol):
                                        if (-1<i<10 and -1<j<10) and self.sell(i,j)!=SeaMap.map_markers[2]:self.seamap[i][j]=SeaMap.map_markers[1]
                                if direction==1: steprow+=1
                                elif direction==0: stepcol+=1     
            else: print(SeaMap.messages[0])                            
        else: print(SeaMap.messages[1])

    def sell(self,row,col):
        if(0<=row<=10 and 0<=col<=10):
            return self.seamap[row][col]
        else: print(SeaMap.messages[1])