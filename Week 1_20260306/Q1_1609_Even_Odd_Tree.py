# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Find element in root
        if not root :
            return True
        queue = deque([root])
        tree = []
        

        while queue :
            current_level = []
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                current_level.append(node.val)
                # 這是更下一層 順序會影響查詢的左到右或右到左
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            tree.append(current_level)                
        
        # level會記下最後一層的長度
        for i in range(len(tree)):
            current_level = tree[i]
            # 比大小    
            for j in range(len(current_level)) :
                if i % 2 == 0 :
                    if current_level[j] % 2 == 0:
                        return False
                    
                if i % 2 != 0 :
                    if current_level[j] % 2 != 0:    
                        return False
            
            for j in range(len(current_level)-1):
                if i % 2 != 0:
                    if (current_level[j] <= current_level[j+1]) :
                        return False
                if i % 2 == 0:
                    if (current_level[j] >= current_level[j+1]):
                        return False
        return True
