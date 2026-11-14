import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, bw = 8, 8
for i in range(9):
    box(ax, x0 + i * bw, 22, bw, 9, 'autre' if i == 0 else 'sujet', r=0.3, lw=0.7)
    for j in range(1, 4):
        line(ax, [(x0 + i * bw + j * bw / 4, 22.6), (x0 + i * bw + j * bw / 4, 24.6)], 'fixe', lw=0.4)
brace(ax, x0, x0 + bw, 31, 'autre', label='4', down=False)
brace(ax, x0, x0 + 9 * bw, 22, 'sujet', label='36', down=True)
text(ax, 44, 51, '36 contient 9 fois 4', 'resultat', 'm', weight='bold')
text(ax, 60, 41, '9 paquets de 4', 'sujet', 's')
save(fig, '09-028')
