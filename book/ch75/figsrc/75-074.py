import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 14
for ox, pts, role, lab in [(8, [(0,0),(1,0),(1,1),(0,1)], 'fixe', 'avant'), (52, [(0,0),(1,0),(2,1),(1,1)], 'sujet', 'après')]:
    P = lambda x, y, ox=ox: (ox + x * u, 16 + y * u)
    poly(ax, [P(*p) for p in pts], role)
    text(ax, (P(0,0)[0] + P(1.5 if ox > 8 else 1, 0)[0]) / 2 + (3 if ox > 8 else -2), 16 + u / 2, 'aire 1', role, 's')
    text(ax, P(0.5, 0)[0] + (0 if ox == 8 else 7), 11, lab, role, 's')
arrow(ax, (8, 16 + u + 4), (48, 16 + u + 4), 'varie', curve=-0.25)
text(ax, 28, 16 + u + 12, 'glisse selon u', 'varie', 's')
arrow(ax, (54, 16 + u + 4), (54 + u, 16 + u + 4), 'sujet', lw=1.4); text(ax, 54 + u + 4, 16 + u + 4, r'$u$', 'sujet', 'm')
text(ax, 44, 4, 'même aire : B est gardée', 'resultat', 's')
save(fig, '75-074')
