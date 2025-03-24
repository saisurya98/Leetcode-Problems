class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        res = [[0 for j in range(len(img[0]))] for i in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                grayscale = self.greyscaleval(img, i, j)

                res[i][j] = grayscale
        return res

    def greyscaleval(self, img: list[list[int]], r: int, c: int) -> int:
        sum_of_neighbours = 0
        count = 0
        m = len(img)
        n = len(img[0])
        # Same,U,D,L,R,UL,UR,DL,DR
        dirs = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        for direction in dirs:
            new_row = r + direction[0]
            new_col = c + direction[1]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n:
                sum_of_neighbours += img[new_row][new_col]
                count += 1
        return int(sum_of_neighbours / count)




sol=Solution()
print(sol.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
