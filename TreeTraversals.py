class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

class Solution(object):

    def levelTraversal(self,root):
        result = []
        queue = [root]
        if not root:
            return []
        while len(queue) != 0:
            level_value = []
            level_node = []
            while len(queue) != 0:
                level_node.append(queue.pop(0))
            for node in level_node:
                level_value.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_value)
        return result


    def inorderTraversal(self,root):
        res=[]
        stack=[]

        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                val=stack.pop()
                res.append(val.data)
                root=val.right

        return res


    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res=[]
        self.depthFirst(root,res)
        return res

    def preorderiterative(self, root):
        res=[]
        stack=[]

        while stack or root:

            if root:
                res.append(root.data)
                stack.append(root)
                root=root.left

            else:
                root=stack.pop().right
        return res
    def depthFirst(self,root,res):

        if root:
            res.append(root.data)
            self.depthFirst(root.left,res)
            self.depthFirst(root.right, res)

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
a=[1,2,3,4]
sol=Solution()

print(sol.levelTraversal(root))