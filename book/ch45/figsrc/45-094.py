import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = ['0 1 2 3', '1 2 3 0', '2 3 0 1', '3 0 1 2']
text(ax, 15, 57, 'les 4 lignes', 'sujet', 'm'); text(ax, 63, 57, r'$S_4$ : 24', 'fixe', 'm')
box(ax, 39, 10.5, 47, 43, 'fixe', fill=False)
for r in range(4):
    yb = 45.5 - r * 11
    box(ax, 2, yb - 1.5, 27, 9, 'sujet', label=r'$%d_L$ : %s' % (r, rows[r]), size='s')
    for c in range(6):
        box(ax, 41 + c * 7.4, yb, 6, 6, 'sujet' if c == 0 else 'fixe', r=0.3)
    arrow(ax, (30, yb + 3), (40.5, yb + 3), 'varie')
text(ax, 44, 4.5, '4 éléments sur 24', 'sujet', 's')
save(fig, '45-094')
