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
            c1, c2 = stack[c], stack[c+1]
            if self.will_these_guys_be_a_fleet(target, c1, c2):
                stack.remove(c1) if c1[1] > c2[1] else stack.remove(c2)
            else:
                c += 1

        return len(stack)