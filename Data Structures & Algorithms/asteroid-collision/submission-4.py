class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = deque()
        stack.append(asteroids[0])


        for idx in range(1, len(asteroids)):

            asteroid = asteroids[idx]

            if not stack:
                stack.append(asteroid)
                continue

            if ((stack[-1] < 0 and asteroid < 0) or # both go left
                (stack[-1] > 0 and asteroid > 0) or # both go right
                (stack[-1] < 0 and asteroid > 0)): # astroids wont collide
                stack.append(asteroid)
                continue
            
            # The only other option is a collision at the top
            # With a collision there are 3 options:
            # 1) moving right wins
            # 2) moving left wins
            # 3) both of the same, both loose
            flag = False
            while stack:
                collision = stack.pop()
                # 3) both are the same, both loose
                if (collision + asteroid == 0):
                    flag = True
                    break
                # 1) asteroid coming right wins
                if collision > 0 and abs(collision) > abs(asteroid):
                    stack.append(collision)
                    break
                # We are now all moving in the same direction
                if collision < 0:
                    stack.append(collision)
                    stack.append(asteroid)
                    break
            # We eliminated everything, add the asteroid coming left to the stack
            # If there was not a collision at the end that removed it.
            if not stack and not flag:
                stack.append(asteroid)

        return list(stack)
                




        
