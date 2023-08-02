"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #16 - Is racecar bounded? (isracecarbounded.py)


Author: Koneshka Bandyopadhyay

Difficulty Level: 8/10


Prompt: You are competing for a GrandPrix with other racecars and
to make things interesting, there are multiple ways to get to the 
finish line. However, some pathways may lead to traps, or loops.
Your job is to identify if your racecar is stuck in a circle or loop.
On an infinite plane, a racecar initially stands at [0, 0] and faces north.
Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such 
that the robot never leaves the circle.

HINT: in simple words, it forms a loop that includes the point of [0,0] (starting point).
However, remember that the loop may be formed with multiple executions of the instructions
and not just one. Keep in mind that a circle can take multiple runs
of the same instruction to form.

Test Cases:
Input: "GG" Output: False
This will yield false as it simply goes in one direction and isn't bounded by any "circle" in the plane.


Input: "GLL" Output: True
This will yield true even though it doesn't form a circle in the first execution,
after multiple executations, it will eventually reach the starting position of [0,0] 
and form a loop after the 2nd execution.

Input: "GLGGRRGG" Output: True
This will yield true even though it doesn't form a circle in the first execution,
after multiple executations, it will eventually reach the starting position of [0,0] 
and form a loop after the 4th execution. Figure out why it's after the 4th execution.
    """

class Solution:
    def isracecarbounded(self, instructions):
        # Initialize the current position and direction of the racecar.
        initial_pos = [0, 0]
        cur_pos = [0, 0]
        cur_dir = 2

        # Iterate over the instructions one by one.
        for instruction in instructions:
            if instruction == "G":
                cur_pos[0] += 1 if cur_dir == 3 else -1 if cur_dir == 1 else 0
                cur_pos[1] += 1 if cur_dir == 2 else -1 if cur_dir == 0 else 0
            elif instruction == "L":
                cur_dir = (cur_dir +1) % 4
            else:
                cur_dir = (cur_dir - 1) % 4
        if cur_pos == initial_pos:
            return True
        else:
            return False
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.isracecarbounded(input1)
    print(ans)

if __name__ == "__main__":
    main()
