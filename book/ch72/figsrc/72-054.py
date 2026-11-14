import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cols = [55, 66, 77]
heads = ['linéaire', 'bijective', 'garde $B$']
for x, h in zip(cols, heads):
    text(ax, x, 56, h, 'fixe', 's', rot=0) if False else None
for i, h in enumerate(['linéaire', 'bijective', 'garde la mesure']):
    text(ax, 4, 52 - i * 0, '', 'fixe', 's') if False else None
# rows
rows = [(40, 'sujet', 'isométrie', ['resultat'] * 3), (14, 'varie', r'$(a,b)\mapsto(2a,b)$', ['resultat', 'resultat', 'limite'])]
heads = ['linéaire', 'bijective', 'garde $B$']
xs = [36, 54, 72]
for x, h in zip(xs, heads):
    text(ax, x, 58, h, 'fixe', 's')
for y, role, lab, st in rows:
    box(ax, 2, y - 7, 22, 14, role, label=None)
    text(ax, 13, y, lab, role, 's')
    for x, r in zip(xs, st):
        disc(ax, x, y, 4, r)
text(ax, 72, 25, r'$(1\ ;\ 0)$ : carré 1 $\to$ 4', 'limite', 's')
text(ax, 54, 2.5, 'une isométrie a les trois', 'sujet', 's')
save(fig, '72-054')
