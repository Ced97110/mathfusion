import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s = 2.8
text(ax, 27, 55, 'grillage', 'varie', 'l'); text(ax, 69, 55, 'gazon', 'resultat', 'l')
box(ax, 10, 24, 12 * s, 8 * s, 'sujet', r=0.3)
line(ax, [(10, 24), (10 + 12 * s, 24), (10 + 12 * s, 24 + 8 * s), (10, 24 + 8 * s), (10, 24)], 'varie', lw=2.2)
box(ax, 52, 24, 12 * s, 8 * s, 'resultat', r=0.3)
for i in range(13): line(ax, [(52 + i * s, 24), (52 + i * s, 24 + 8 * s)], 'resultat', lw=0.4)
for j in range(9): line(ax, [(52, 24 + j * s), (52 + 12 * s, 24 + j * s)], 'resultat', lw=0.4)
for x0 in (10, 52):
    text(ax, x0 + 6 * s, 20.5, '12 m', 'sujet', 's'); text(ax, x0 - 1, 24 + 4 * s, '8 m', 'sujet', 's', ha='right')
text(ax, 27, 14, r'$2\times12+2\times8$', 'varie', 's'); text(ax, 27, 7, '= 40 m', 'varie', 'm')
text(ax, 69, 14, r'$12\times8$', 'resultat', 's'); text(ax, 69, 7, '= 96 m²', 'resultat', 'm')
save(fig, '11-142')
