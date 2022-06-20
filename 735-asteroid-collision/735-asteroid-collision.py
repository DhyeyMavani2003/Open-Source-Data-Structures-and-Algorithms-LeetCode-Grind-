class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast > 0: # save asteroid moving right until future collisions
                stack.append(ast)
            else: # asteroid moving left, check for collisions
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop() # smaller asteroids destroyed

                if stack and stack[-1] > 0 and stack[-1] == -ast:
                    stack.pop() # mutual destruction
                elif not stack or stack[-1] < 0:
                    stack.append(ast) # leftward asteroid remains so save on stack

        return stack