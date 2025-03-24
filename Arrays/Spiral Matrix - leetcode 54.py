class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        TOP_BOUNDARY=0
        BOTTOM_BOUNDARY=len(matrix)
        LEFT_BOUNDARY=-1
        RIGHT_BOUNDARY=len(matrix[0])
        row=0
        col=0
        up,right,down,left=0,1,2,3
        current_state=right
        if matrix is None or len(matrix)==0:
            return []
        res=[]
        while len(res)!=len(matrix)*len(matrix[0]):
            if current_state==right:
                while col<RIGHT_BOUNDARY:
                    res.append(matrix[row][col])
                    col+=1
                RIGHT_BOUNDARY-=1
                row+=1
                col-=1
                current_state=down
            elif current_state==down:
                while row<BOTTOM_BOUNDARY:
                    res.append(matrix[row][col])
                    row+=1
                BOTTOM_BOUNDARY-=1
                row-=1
                col-=1
                current_state=left
            elif current_state==left:
                while col>LEFT_BOUNDARY:
                    res.append(matrix[row][col])
                    col-=1
                LEFT_BOUNDARY+=1
                row=row-1
                col=col+1
                current_state=up
            else:
                while row>TOP_BOUNDARY:
                    res.append(matrix[row][col])
                    row-=1
                TOP_BOUNDARY+=1
                row=row+1
                col=col+1
                current_state=right
        return res