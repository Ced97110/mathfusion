import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'chercher $n$ tel que $n\cdot1=0$', 'sujet', 'm')
for i, (n, s) in enumerate([(1, '1'), (2, '2'), (3, '3'), (100, '100'), (1000, r'1\,000')]):
    y = 48 - 8.5 * i
    box(ax, 4, y, 44, 7, 'sujet', label=r'$%s\cdot1=%s$' % (s, s))
    arrow(ax, (48.5, y + 3.5), (59.5, y + 3.5), 'fixe')
    box(ax, 60, y, 20, 7, 'limite', label=r'$\neq0$')
box(ax, 8, 1, 72, 8, 'resultat', label='aucun entier : char = 0')
save(fig, '51-132')
