class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): # x는 ㅣ0에서 작으면 False
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10 # x가 0에서 값이 많을떄  revertedNumber 곱하기 10 + x를 10에 나눌때 남는 값
            x //= 10  #마지막 숫자를 없애기 
        return x == revertedNumber or x == revertedNumber // 10
