# Algorithms from https://leetcode.com/studyplan/top-interview-150/
# Check out my Profile https://leetcode.com/TobiasWiSoftware

# <--------------------------------------- Chapter Two Pointers level easy ----------------------------->

from typing import List, Optional


print("Task 125. Valid Palindrome - A palindrome is a word, where all non-alphanumeric chars are removed and reads the same forward and backward")

inputList = ["A man, a plan, a canal: Panama", "race a car"]

def isPalindrome(s: str) -> bool:
    isResult = True
    i = 0
    j = len(s) - 1
    
    while i < j:
        c1 = s[i].lower()
        c2 = s[j].lower()
        
        if c1.isalnum() and c2.isalnum():
            if c1 != c2:
                isResult = False
                break
        else:
            i = i + 1 if not c1.isalnum() else i
            j = j - 1 if not c2.isalnum() else j
            continue
        i = i + 1
        j = j - 1
    return isResult

for s in inputList:
    print("Test case: " + s + "\n" + "Result: " + ("is a Palindrome" if isPalindrome(s) else "is not a Palindrome"))

print("\n" + "Beats 30 % of users in runtime and 74 % in space - O(n) time and O(n) space")

print("\n\n")

print("Task 392. Is Subsequence - check if s is a subsequence of t by maintainig the right order")
print()

inputTuples = [("abc", "ahbgdc"), ("axc", "ahbgdc")]

def isSubsequence(s: str, t: str) -> bool:
   
    i = 0
    x = 0
   
    while(i < len(s) and x < len(t)):
       if t[x] == s[i]:
           i = i + 1
           x = x + 1
       else:
           x = x + 1
           
    return i == len(s)

for tuple in inputTuples:
    print("The testcase is " + tuple[0] + " " + tuple[1] + " and the result is " + str(isSubsequence(tuple[0], tuple[1])))
    
print("\n" + "Is better than 46 % of users in runtime and 35 % in space - runtime O(n) ans space O(1)")

print("\n\n")

print("Task 167. Two Sum II - find the two numbers that add up to target - constraint: Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.")
   
inputTupless = [([2,3,4], 6), ([-1,0], -1)]

def twoSum(numbers: List[int], target: int) -> List[int]:
    result = []
    i = 0
    t = len(numbers) - 1
    
    while(i < t):
        ta = numbers[i] + numbers[t]
        if ta == target:
           result.append(i + 1)
           result.append(t + 1)
           break
        elif ta > target:
            t = t - 1
        else:
            i = i + 1
            
    return result

for tu in inputTupless:
    print("Numbers " + str(tu[0]) + " target " + str(tu[1]) + " with the result " + str(twoSum(tu[0], tu[1])))

# Beats 93 % in runtime and 73 % in space

print("\n\n")

print("Task 11. Container with most water: Given the numbers in an array representing the hight of a box and the lenth count the width. Return the max. Volume possible")
print()

inputList = [1,8,6,2,5,4,8,3,7]

def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    maxValue = 0
    while(left < right):
        maxValue = min(height[left], height[right]) * (right - left) if min(height[left], height[right]) * (right - left) > maxValue else maxValue
        mini = min(height[left],height[right])
        if mini == height[left]: left = left + 1
        if mini == height[right]: right = right - 1
    
    return maxValue

print("The input is " + str(inputList) + " the result is " + str(maxArea(inputList)))

# Beats 36 % in runtime and 61 % in memory

print("\n\n") 



# <------------------------------------ Chapter Binary Tree --------------------------------------->
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


print("Task 104. Maximum depth of a binary tree")        
print()

root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7))) # 3 start node, points on 9 and 20. 9 has none, none. 20 has 15,7
#root = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(5)),None))

def maxDepth(root: Optional[TreeNode]) -> int:
    depth = 1
    if root != None:
        return max(recussiveRoot(root.left, depth), recussiveRoot(root.right, depth))
    return depth - 1
    
    

def recussiveRoot(root: Optional[TreeNode], depth: int) -> int:
    if root != None:
            return max(recussiveRoot(root.right, depth + 1), recussiveRoot(root.left, depth + 1))
    else:
        return depth - 1
    
print("The result is " + str(maxDepth(root)))

# Beats 85 % in runtime and 44 % in space

print("\n\n")   

print("Task 100. Same binary Tree")
print()

inputT1 = TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))
inputT2 = TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))
inputT3 = TreeNode(1,TreeNode(2),None)

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p == None and q == None:
        return True
    elif p != None and q == None or p == None and q != None:
        return False
    
    if p.val != q.val:
        return False    

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
           
print("The input is " + str(inputT1) + " and " + str(inputT2) + " and the result " + str(isSameTree(inputT1, inputT2)))
print("The result is " + str(isSameTree(inputT1, inputT3)))
# 38 % in runtime and 31% in memory 

print("Task 226. Invert the binary Tree")

inputTree = TreeNode(4,TreeNode(2,TreeNode(1,None,None),TreeNode(3,None,None)),TreeNode(7,TreeNode(6,None,None),TreeNode(9,None,None)))

def invertTree(root: Optional[TreeNode], nodeMarker = None) -> Optional[TreeNode]:
    if root == None:
        return None
    
    if nodeMarker == None:
        nodeMarker = root
    
    temp = root.left
    root.left = root.right
    root.right = temp
        
    invertTree(root.left,nodeMarker)
    invertTree(temp,nodeMarker)
    
    return nodeMarker
    
# Beats 51% in Runtime and 95% in Memory - runtime O(n), Space complex O(log(n))

print()
print("Task 101. Symmetric binary Tree")

inputTree1 = TreeNode(1,TreeNode(2,TreeNode(3,None,None),TreeNode(4,None,None)), TreeNode(2,TreeNode(4,None,None),TreeNode(3,None,None)))
inputTree2 = TreeNode(1,TreeNode(2,None,TreeNode(3,None,None)),TreeNode(2,None,TreeNode(3,None,None)))

def isSymetric(root: Optional[TreeNode]) -> bool:
    if root == None:
        return True
    else:
        return isSame(root.left, root.right)
   
def isSame(leftroot, rightroot) -> bool:
    if leftroot == None and rightroot == None:
        return True
    
    if leftroot == None or rightroot == None:
        return False
    
    if leftroot.val != rightroot.val:
        return False
    
    return isSame(leftroot.left, rightroot.right) and isSame(leftroot.right, rightroot.left) 
    
print("First Tree symetric: " + str(isSymetric(inputTree1)))
print("Second Tree symetric " + str(isSymetric(inputTree2)))

# Beats 56 % in runtime and 99 % in space
