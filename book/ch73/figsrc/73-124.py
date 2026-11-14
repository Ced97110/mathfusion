import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
p, gx, gy = 10, 14, 6
for i in range(1, 4):
    for j in range(1, 4):
        v, r = ('1', 'sujet') if i == j else (('5', 'varie') if (i, j) == (3, 2) else ('0', 'fixe'))
        box(ax, gx + (j - 1) * p, gy + (3 - i) * p, p - 1, p - 1, r, label=v)
text(ax, 28.5, 44, r'$T_{32}(5)$', 'varie', 'l')
arrow(ax, (46, 25), (46, 15), 'varie')
text(ax, 68, 20, 'ajoute 5 fois\nla ligne 2\nà la ligne 3', 'varie', 's')
save(fig, '73-124')
