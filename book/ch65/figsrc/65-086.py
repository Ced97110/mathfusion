import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
panels = [
    (2, r'échange $(12)$', [('fixe', r'$t_1$ : 14 → 14'), ('varie', r'$t_2$ : 11 → 10'), ('varie', r'$t_3$ : 10 → 11')], 'limite', r'fixe $t_1$ seul : pas dans $V$'),
    (46, r'échange $(12)(34)$', [('fixe', r'$t_1$ : 14 → 14'), ('fixe', r'$t_2$ : 11 → 11'), ('fixe', r'$t_3$ : 10 → 10')], 'resultat', r'fixe les trois : dans $V$'),
]
for x, head, rows, vrole, verdict in panels:
    text(ax, x + 20, 64, head, 'sujet', 'm')
    for j, (role, lab) in enumerate(rows):
        box(ax, x, 46 - j * 12, 40, 9, role, label=lab, size='s')
    box(ax, x, 6, 40, 11, vrole, label=verdict, size='s')
    arrow(ax, (x + 20, 21), (x + 20, 18), vrole)
save(fig, '65-086')
