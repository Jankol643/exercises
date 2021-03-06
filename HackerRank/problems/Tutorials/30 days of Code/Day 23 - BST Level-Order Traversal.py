#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-binary-trees
# Difficulty: Easy

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        nodes_to_search = list() # queue with nodes to visit
        nodes_traversed = '' # result string with data of nodes
        nodes_to_search.append(root)
        while len(nodes_to_search) > 0:
            node = nodes_to_search.pop(0)
            if node.left != None:
                nodes_to_search.append(node.left)
            if node.right != None:
                nodes_to_search.append(node.right)
            nodes_traversed += str(node.data) + ' '
        print(nodes_traversed)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
