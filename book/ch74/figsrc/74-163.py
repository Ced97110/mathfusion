import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(12, 'sujet', r'p6m : $D_6$, 12 éléments'), (8, 'autre', r'p4m : $D_4$, 8 éléments'), (1, 'fixe', r'p1 : $C_1$, 1 élément')]
y = 47
for n, role, lab in rows:
    text(ax, 3, y + 8, lab, role, 'm', ha='left')
    for i in range(n):
        box(ax, 3 + i * 6.6, y, 5.8, 5.8, role, r=0.4)
    y -= 20
save(fig, '74-163')
