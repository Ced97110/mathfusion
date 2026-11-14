import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
n = 5
text(ax, 2, 74, 'image de :', 'encre', 's', ha='left')
for c in range(n):
    x = 24 + c * 14
    text(ax, x, 74, str(c + 1), 'sujet', 'm')
    if c == 1:
        box(ax, x - 6, 14, 12, 56, 'varie', fill=False, lw=1.2)
    for r in range(n):
        taken = r < c
        disc(ax, x, 64 - r * 9, 3, 'fixe' if taken else 'sujet', fill=True)
    text(ax, x, 8, str(n - c), 'resultat' if c != 1 else 'varie', 'm', weight='bold')
text(ax, 2, 8, 'choix :', 'encre', 's', ha='left')
text(ax, 38, 77.5, '', 'encre', 's')
text(ax, 44, 1.5, '', 'encre', 's')
text(ax, 44, 2, 'gris : image déjà prise', 'fixe', 's')
save(fig, '44-121')
