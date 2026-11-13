import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
cols = [(r'$\emptyset$', r'$\{a,b,c\}$'), (r'$\{a\}$', r'$\{b,c\}$'), (r'$\{b\}$', r'$\{a,c\}$'), (r'$\{a,b\}$', r'$\{c\}$')]
text(ax, 44, 59, r'idéal $K$ : parties sans $c$', 'sujet', 'm')
text(ax, 44, 7, r'compléments, hors de $K$', 'fixe', 'm')
for i, (top, bot) in enumerate(cols):
    x = 4 + 21 * i
    box(ax, x, 38, 19, 9, 'sujet', label=top)
    box(ax, x, 12, 19, 9, 'fixe', label=bot)
    arrow(ax, (x + 9.5, 37.4), (x + 9.5, 21.6), 'varie', both=True)
text(ax, 44, 29.5, r"un seul des deux est dans $K$", 'resultat', 's')
save(fig, '80-337')
