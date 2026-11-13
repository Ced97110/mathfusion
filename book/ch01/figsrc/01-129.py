import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
line(ax, [(40,62),(48,56),(40,50)], 'sujet', lw=2.5)
text(ax, 37, 56, 'ouvert : plus grand', 'sujet', 's', ha='right')
text(ax, 51, 56, 'pointe : plus petit', 'sujet', 's', ha='left')
text(ax, 44, 42, '« strictement » : égal exclu', 'fixe', 's')
s = 3.6
for i in range(9):
    box(ax, 8 + s*i, 28, s, s, 'resultat' if i == 8 else 'fixe', r=0.2, lw=0.5)
for i in range(8):
    box(ax, 8 + s*i, 23.5, s, s, 'fixe', r=0.2, lw=0.5)
text(ax, 5, 29.8, '9', 'fixe', 's'); text(ax, 5, 25.3, '8', 'fixe', 's')
text(ax, 24, 14, '9 > 8 : vrai', 'resultat', 'l')
for i in range(9):
    box(ax, 47 + s*i, 28, s, s, 'fixe', r=0.2, lw=0.5)
    box(ax, 47 + s*i, 23.5, s, s, 'fixe', r=0.2, lw=0.5)
box(ax, 47 + s*9, 28, s, s, 'limite', fill=False, r=0.2, lw=0.8, dash=True)
text(ax, 44.5, 29.8, '9', 'fixe', 's'); text(ax, 44.5, 25.3, '9', 'fixe', 's')
text(ax, 63, 14, '9 > 9 : faux', 'limite', 'l')
save(fig, '01-129')
