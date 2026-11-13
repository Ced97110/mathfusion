import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# (famille, libre ?, atteint tout le plan ?)
rows = [(r'$(1,0)$', True, False), (r'$(1,0),\ (0,1),\ (1,1)$', False, True), (r'$(1,0),\ (0,1)$', True, True)]
text(ax, 56, 57, 'libre', 'fixe', 'm')
text(ax, 77, 57, 'atteint', 'fixe', 'm')
text(ax, 77, 52.5, 'tout le plan', 'fixe', 's')
for (fam, libre, tout), y in zip(rows, [36, 22, 8]):
    box(ax, 2, y, 42, 10, 'sujet', label=fam)
    for x, ok, yes, no in [(56, libre, 'oui', 'non'), (77, tout, 'oui', 'non')]:
        role = 'resultat' if ok else 'limite'
        box(ax, x - 8, y, 16, 10, role, label=yes if ok else no)
save(fig, '58-148')
