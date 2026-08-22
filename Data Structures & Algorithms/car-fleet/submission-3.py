class Solution:
    def will_these_guys_be_a_fleet(self, t, c1, c2) -> bool:
       return (t - c1[0]) / c1[1] >= (t - c2[0]) / c2[1]
        
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            p, s = position[i], speed[i]
            cars.append([p, s])

        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        stack = cars.copy()

        c = 0
        while c < len(stack)-1:
            c1, c2 = stack[c], stack[c+1]
            if self.will_these_guys_be_a_fleet(target, c1, c2):
                stack.remove(c1) if c1[1] > c2[1] else stack.remove(c2)

                c -= 1

            c += 1

        return len(stack)