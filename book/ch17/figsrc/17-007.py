import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 8, 74, 24, 0, 8, every=2, arrow_right=True)
text(ax, 84, 30, r'$d$', 'fixe', 's')
for v, p, role in [(2.5, 8, 'resultat'), (4, 11, 'resultat'), (6, 15, 'resultat'), (7, 17, 'limite')]:
    disc(ax, f(v), 24, 1.9, role)
    line(ax, [(f(v), 27), (f(v), 33)], role, lw=0.7)
    text(ax, f(v), 37, f'{p} €', role, 's')
text(ax, 22, 51, 'permis : 15 € ou moins', 'resultat', 's')
text(ax, 62, 51, 'interdit', 'limite', 's')
save(fig, '17-007')
