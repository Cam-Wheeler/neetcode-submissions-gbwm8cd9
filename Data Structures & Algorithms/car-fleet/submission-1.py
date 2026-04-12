class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for idx in range(len(position)):
            cars.append((position[idx], (target - position[idx]) / speed[idx]))
        
        cars = sorted(cars, key=lambda x: x[0], reverse=True)

        stack = []
        for car in cars:
            if not stack:
                stack.append(car)
            else:
                if car[1] > stack[-1][1]:
                    stack.append(car)
        return len(stack)