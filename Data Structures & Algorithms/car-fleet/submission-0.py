class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i, p in enumerate(position):
            cars.append([p, speed[i]])
        cars.sort()
        i = 0
        stack.append((target - cars[-1][0]) / cars[-1][1])
        for i in range(len(cars)-2, -1, -1):
            stops = (target - cars[i][0]) / cars[i][1]    
            if stops > stack[-1]:
                stack.append(stops)
            
        return len(stack)
