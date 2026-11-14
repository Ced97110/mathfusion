import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
c, g = 9, 1.2
text(ax, 44, 51, r'$k$ modulo 8', 'fixe', 's')
order = [1, 3, 5, 7, 2, 4, 6]
x = 4
pos = {}
for n, k in enumerate(order):
    if n == 4: x += 5
    pos[k] = x
    box(ax, x, 28, c, 11, 'resultat' if k % 2 else 'limite', label=str(k), r=0.4)
    x += c + 1.2
l0, l1 = pos[1], pos[7] + c
brace(ax, l0, l1, 26, 'resultat', label='PGCD avec 8 = 1', down=True)
brace(ax, pos[2], pos[6] + c, 26, 'limite', label='PGCD > 1', down=True)
text(ax, (l0 + l1) / 2, 8, 'inverse', 'resultat', 'm', weight='bold')
text(ax, (pos[2] + pos[6] + c) / 2, 8, 'pas d’inverse', 'limite', 'm', weight='bold')
save(fig, '44-167')
