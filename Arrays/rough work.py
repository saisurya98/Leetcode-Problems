class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m=len(mat)
        n=len(mat[0])
        row,col=0,0
        direction=1
        res=[]
        while len(res)!=m*n:
            # r-0,c-0 [1]
            #r-0,c-1 ,dir=-1 [1,2]
            #r-1,c-0
            res.append(mat[row][col])
            if direction==1:
                if col==n-1:
                    direction=-1
                    row+=1
                elif row==0:
                    direction = -1
                    col+=1
                else:
                    row-=1
                    col+=1
            else:
                if col==0:
                    direction = 1
                    row+=1
                elif row==m-1:
                    direction = 1
                    col+=1
                else:
                    row+=1
                    col-=1
        return res



sol=Solution()
print(sol.findDiagonalOrder( [[1,2,3],[4,5,6],[7,8,9]]))




