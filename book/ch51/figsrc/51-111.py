import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 22, 52, 28, 16, 'sujet'); text(ax, 36, 63, 'sans diviseur', 'sujet', 's'); text(ax, 36, 57, 'de zéro', 'sujet', 's')
box(ax, 62, 52, 24, 16, 'autre'); text(ax, 74, 63, 'on peut', 'autre', 's'); text(ax, 74, 57, 'simplifier', 'autre', 's')
arrow(ax, (50.8, 60), (61.2, 60), 'varie', both=True, lw=1.4); text(ax, 56, 64, r'$\Leftrightarrow$', 'varie', 'l')
text(ax, 11, 44, 'le même anneau', 'fixe', 's', ha='center') if False else None
for y, name, ok, role, mark in [(34, r'dans $\mathbb{Z}$', 'oui', 'resultat', '2 fois 3 = 6'), (14, r'dans $\mathbb{Z}/4$', 'non', 'limite', '2 fois 2 = 0')]:
    box(ax, 2, y - 8, 14, 16, 'fixe'); text(ax, 9, y, name, 'fixe', 's') if False else None
    text(ax, 9, y, name.replace('dans ', ''), 'fixe', 'm')
    box(ax, 22, y - 8, 28, 16, role, label=ok, size='l')
    box(ax, 62, y - 8, 24, 16, role, label=ok, size='l')
line(ax, [(2, 45), (86, 45)], 'fixe', lw=0.5)
save(fig, '51-111')
