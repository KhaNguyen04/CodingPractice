class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # BFS Djsktra 
        queue=[]
        # sum,row,col
        queue.append((grid[0][0],0,0))
        rec=[[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dirs=((1,0),(0,1))
        rec[0][0]=grid[0][0]
        while queue:
            total,r,c=heapq.heappop(queue)

            if r==len(grid)-1 and c==len(grid[0])-1:
                return total
            for dir in dirs:
                nr,nc=r+dir[0],c+dir[1]
                if nr<0 or nr>=len(grid) or nc<0 or nc>=len(grid[0]):
                    continue
                path=total+grid[nr][nc]
                if path>=rec[nr][nc]:
                    continue
                rec[nr][nc]=path
                heapq.heappush(queue,(path,nr,nc))


            