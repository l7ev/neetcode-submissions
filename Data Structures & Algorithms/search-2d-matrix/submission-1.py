class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mLow, mHigh = 0, len(matrix) -1

        while mHigh >= mLow:
            mMiddle = (mHigh + mLow) // 2

            rLow, rHigh = 0, len(matrix[mMiddle]) -1
            if target > matrix[mMiddle][rHigh]:
                mLow = mMiddle +1
            elif target < matrix[mMiddle][rLow]:
                mHigh = mMiddle -1
            
            else:
                while rHigh >= rLow:
                    middle = (rHigh + rLow) // 2

                    if matrix[mMiddle][middle] > target:
                        rHigh = middle -1
                    elif matrix[mMiddle][middle] < target:
                        rLow = middle +1
                    else: return True
                return  False
        return False
                     