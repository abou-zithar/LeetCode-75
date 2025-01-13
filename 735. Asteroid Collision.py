class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        
        for ast in asteroids:
            while answer and ast < 0 < answer[-1]:              
                if abs(ast) > abs(answer[-1]):
                    answer.pop()
                elif abs(ast) == abs(answer[-1]):
                    answer.pop()
                    break
                else:
                    break
            else:
                answer.append(ast)

        return answer
            
       