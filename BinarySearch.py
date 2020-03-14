class Solution(object):
    def binary_search(self, matrix,target,start,vertical):
        low = start
        high = len(matrix[0])-1 if vertical else len(matrix)-1
        
        while high >= low:
            mid = (low + high) // 2 #rounded number as return
            if vertical: 
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid -1
                else:
                    return True
                        
        return False


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        for i in range (min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
            
        return False
