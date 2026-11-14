import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$G$ : 8 éléments, 4 classes de 2', 'sujet', 'm')
for k in range(4):
    x = 6 + k * 19
    box(ax, x, 50, 17, 14, 'varie' if k == 0 else 'sujet', fill=False, dash=True, r=1.2)
    for j in range(2):
        disc(ax, x + 4.5 + j * 8, 57, 2.4, 'varie' if k == 0 else 'sujet')
    arrow(ax, (x + 8.5, 48.5), (x + 8.5, 33.5), 'fixe')
    disc(ax, x + 8.5, 29, 2.8, 'sujet')
text(ax, 15, 67.5, r'$C$ : le centre', 'varie', 's')
text(ax, 44, 20, r'$G/C$ : 4 éléments', 'sujet', 'm')
box(ax, 8, 3, 72, 10, 'resultat', label=r"$C\neq\{e\}$ : abélien et normal", size='s')
save(fig, '64-107')
