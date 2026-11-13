import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cols = [(15, 'mêmes unités', '13', '13 R 13 : oui', True),
        (44, 'frère de', r'$a$', r'$a\ R\ a$ : non', False),
        (73, 'plus grand que', '5', '5 > 5 : non', False)]
for x, name, d, res, ok in cols:
    text(ax, x, 49, name, 'fixe', 's')
    role = 'resultat' if ok else 'limite'
    disc(ax, x, 28, 5, 'sujet', label=d, size='m')
    arrow(ax, (x-3.5, 32.5), (x+3.5, 32.5), role, curve=-1.6)
    text(ax, x, 12, res, role, 's')
save(fig, '43-024')
