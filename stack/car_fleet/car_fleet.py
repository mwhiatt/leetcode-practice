class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        tuples = [(pos, speed) for pos, speed in zip(position, speed)]
        tuples.sort(reverse=True)
        stack = []
        for pos, speed in tuples:
            stack.append((target - pos)/speed)
            while len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# d = r * t
# d = target - pos[i]
# t = (target - pos[i])/r