import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [('sujet', ['2','2','3','5'], 44), ('varie', ['5','3','2','2'], 30), ('autre', ['3','2','2','5'], 16)]
text(ax, 44, 58, r'de 1 à 60 : 4 marches chacune', 'encre', 's')
for role, fs, y in rows:
    for i, f in enumerate(fs):
        box(ax, 4 + i * 21, y - 5, 19, 10, role, label=r'$\times%s$' % f)
text(ax, 44, 4, 'mêmes facteurs : 2, 2, 3, 5', 'resultat', 's')
save(fig, '79-183')
