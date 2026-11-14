import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(65)
names = [('sujet', 'Transformations', r'$\alpha,\ \beta$'), ('autre', 'Entiers naturels', '0, 1, 2'), ('varie', 'Mots', 'ab, ba')]
cw, gap = 26, 3
for i, (role, nm, ex) in enumerate(names):
    x = 2 + i * (cw + gap)
    box(ax, x, 38, cw, 20, role, label=None)
    text(ax, x + cw / 2, 53, nm, role, 's')
    text(ax, x + cw / 2, 44, ex, role, 'm')
    arrow(ax, (x + cw / 2, 38), (44, 25), 'fixe')
box(ax, 8, 6, 72, 19, 'resultat')
text(ax, 44, 20, 'mêmes règles', 'resultat', 'l', weight='bold')
text(ax, 44, 13, 'parenthèses sans effet ; un neutre', 'resultat', 's')
text(ax, 44, 61, 'éléments différents', 'fixe', 's')
save(fig, '44-064')
