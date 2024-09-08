import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

starlight = int(input())
if 620 <= starlight <= 780:
    print('Red')
elif 590 <= starlight < 620:
    print('Orange')
elif 570 <= starlight < 590:
    print('Yellow')
elif 495 <= starlight < 570:
    print('Green')
elif 450 <= starlight < 495:
    print('Blue')
elif 425 <= starlight < 450:
    print('Indigo')
elif 380 <= starlight < 425:
    print('Violet')