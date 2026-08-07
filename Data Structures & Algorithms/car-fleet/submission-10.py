class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        for idx in range(len(position)):
            cars.append((position[idx], (target - position[idx]) / speed[idx]))
        
        cars = sorted(cars, key=lambda x: x[0], reverse=True) # sort based on the distance to the target biggest first!

        stack = []
        for car in cars:
            if not stack:
                stack.append(car)
            else:
                if car[1] > stack[-1][1]: # compare against the tuple at top of the stack.
                    stack.append(car)
        return len(stack)