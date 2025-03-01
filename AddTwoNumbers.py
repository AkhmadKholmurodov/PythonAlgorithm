class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() #dummy 노드 생성
        res = dummy 

        total = carry = 0  #  0 시작값을 가진 토탈 , carry 생성

        while l1 or l2 or carry: #1, l2 중 하나라도 남아있거나 carry가 있으면 계속 진행
            total = carry

            if l1:
                total += l1.val 
                l1 = l1.next # l1이 존재하면 현재 노드의 값을 total에 더하고 l1 다음 노드로 이동함
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10 # 현재 자릿수에 들어갈 값은 total을 10으로 나눈 나머지임
            carry = total // 10 # carry을 total 나누기 10으로 같게 만듬
            dummy.next = ListNode(num) # 새로운 노드를 생성하여 현재 노드의 다음에 연결
            dummy = dummy.next # dummy Pointer 다음 노드로 이동
        
        return res.next    
