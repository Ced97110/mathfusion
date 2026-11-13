import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 14, 56, 60, 10, 'fixe', label='mêmes nombres pairs, mêmes opérations', size='s')
for x, role, name, conv, res, rrole in [(2, 'autre', 'Judson', '1 pas exigé', 'les pairs : un anneau', 'resultat'),
                                        (46, 'sujet', 'ce livre', '1 exigé', 'les pairs : pas un anneau', 'limite')]:
    box(ax, x, 6, 40, 42, role)
    arrow(ax, (x + 20, 56), (x + 20, 48), 'fixe')
    text(ax, x + 20, 42, name, role, 'm', weight='bold')
    text(ax, x + 20, 34, conv, role, 's')
    box(ax, x + 3, 9, 34, 14, rrole, label=res.replace(': ', ':\n'), size='s')
box(ax, 49, 25, 34, 6, 'limite', fill=False, dash=True, label='1 est impair', size='s')
save(fig, '51-092')
