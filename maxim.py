from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def preorder_count(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + preorder_count(root.left) + preorder_count(root.right)

def inorder_count(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return inorder_count(root.left) + 1 + inorder_count(root.right)

def postorder_count(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return postorder_count(root.left) + postorder_count(root.right) + 1

def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order or level_order[0] is None:
        return None
    
    root = TreeNode(level_order[0])
    queue = [root]
    idx = 1
    
    while queue and idx < len(level_order):
        current = queue.pop(0)
        
        if idx < len(level_order) and level_order[idx] is not None:
            current.left = TreeNode(level_order[idx])
            queue.append(current.left)
        idx += 1
        
        if idx < len(level_order) and level_order[idx] is not None:
            current.right = TreeNode(level_order[idx])
            queue.append(current.right)
        idx += 1
    
    return root

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    traverse(root)
    return result

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)
    traverse(root)
    return result
