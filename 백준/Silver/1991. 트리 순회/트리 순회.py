import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 트리 순회 (1991)
1. 이진 트리를 전위/중위/후위 순회한 결과 출력

[풀이]
1. 트리
"""


# 전위 순회
def preorder(parent):
    if parent != '.':
        print(parent, end='')
        preorder(tree[parent][0])
        preorder(tree[parent][1])


# 중위 순회
def inorder(parent):
    if parent != '.':
        inorder(tree[parent][0])
        print(parent, end='')
        inorder(tree[parent][1])


# 후위 순회
def postorder(parent):
    if parent != '.':
        postorder(tree[parent][0])
        postorder(tree[parent][1])
        print(parent, end='')


N = int(input())
# 딕셔너리 구성
tree = {}
for _ in range(N):
    parent, left, right = map(str, input().split())
    tree[parent] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
