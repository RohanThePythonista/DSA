"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
Example 4:

Input: n = 2, pick = 2
Output: 2


Constraints:

1 <= n <= 231 - 1
1 <= pick <= n

"""

"""
Day1: dream big
12/Oct: first time I saw this problem I didn't get at first read 
    ....didn't understand the pick value input to be given in program itself by user in logic
I read it 4 to 5 times to understand it basically
Then once I understood I got that this could be solved using the divide and conquer technique in first go 
    ....basically binary searching algorithm technique ...
I used basic loop to iterate over start<= end and assume middle is what I picked to guess
and pass same to guess api which would tell 0, 1, -1 to check if found, big or less

"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        if n == 1:
            return 1
        start = 1
        end = n
        while start <= end:
            middle = (start + end) // 2
            guessed = guess(middle)
            if guessed == 0:
                return middle
            if guessed == -1:
                end = middle - 1
            if guessed == 1:
                start = middle + 1


def guess(pick: int) -> int:
    global guess_find
    if guess_find == pick:
        return 0
    if guess_find > pick:
        return 1
    return -1


if __name__ == "__main__":
    s = Solution()
    n = int(input())
    guess_find = int(input())
    result = s.guessNumber(n)
    assert (guess_find == result)
    print(f"your guess {result=} is correct")
