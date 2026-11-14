import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
gx, gy, c = 18, 10, 11.5
for a in (1, 2, 3):
    for b in (1, 2, 3):
        x, y = gx + (b-1)*c, gy + (3-a)*c
        yes = a < b
        box(ax, x, y, c-1, c-1, 'sujet' if yes else 'fixe', r=0.4)
        if yes: disc(ax, x+(c-1)/2, y+(c-1)/2, 2.2, 'sujet')
for k in (1, 2, 3):
    text(ax, gx + (k-1)*c + (c-1)/2, gy + 3*c + 2, str(k), 'encre', 's')
    text(ax, gx - 3, gy + (3-k)*c + (c-1)/2, str(k), 'encre', 's')
text(ax, gx + 1.5*c, gy + 3*c + 7, 'second nombre', 'encre', 's')
text(ax, 5, gy + 1.5*c, 'premier', 'encre', 's', rot=90)
box(ax, 56, 38, 30, 9, 'fixe', label='S × S : 9 couples', size='s')
box(ax, 56, 24, 30, 9, 'sujet', label='R : 3 couples', size='s')
text(ax, 71, 15, 'R ⊂ S × S', 'sujet', 's')
save(fig, '43-020')
