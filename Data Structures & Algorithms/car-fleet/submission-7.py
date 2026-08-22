class Solution:
    def will_these_guys_be_a_fleet(self, t, c1, c2) -> bool:
       return (t - c1[0]) / c1[1] >= (t - c2[0]) / c2[1]
        
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            p, s = position[i], speed[i]
            stack.append([p, s])

        stack = sorted(stack, key=lambda x: x[0], reverse=True)

        c = 0
        while c < len(stack)-1:
            car1, car2 = stack[c], stack[c+1]
            if self.will_these_guys_be_a_fleet(target, car1, car2):
                stack.pop(c) if car1[1] > car2[1] else stack.pop(c+1)
            else:
                c += 1

        return len(stack)