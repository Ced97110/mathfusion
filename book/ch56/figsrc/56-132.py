import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 4, 46, 32, 10, 'sujet', label='euclidien')
arrow(ax, (36, 51), (52, 51), 'varie', lw=1.4)
box(ax, 52, 46, 32, 10, 'resultat', label='principal')
text(ax, 44, 55 + 3, '', 'encre', 's')
y = 22
f = numberline(ax, 8, 72, y, 0, 12, step=1, every=2, arrow_right=True)
for v in range(0, 13):
    if v % 2 == 0:
        role = 'sujet' if v in (6, 10) else 'resultat'
        disc(ax, f(v), y, 1.6, role)
text(ax, f(6), y + 6, '6', 'sujet', 's')
text(ax, f(10), y + 6, '10', 'sujet', 's')
text(ax, f(2), y + 6, '2', 'resultat', 's')
text(ax, 44, 8, r'idéal $(6,10)$ : tous les pairs = multiples de $2$', 'resultat', 's')
text(ax, 44, 36, r'$2=6\times 2-10$ : un seul générateur', 'encre', 's')
save(fig, '56-132')
