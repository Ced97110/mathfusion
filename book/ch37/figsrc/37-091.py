import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
D = math.sqrt(984375); k, y0 = 0.5, 24
r, ra, rb, rc = D/75, D/35, D/25, D/15
fig, ax = canvas(64)
box(ax, 14, y0, r*k, ra*k, 'sujet', r=0.3)
text(ax, 14 + r*k/2, y0 - 3.5, r'$r$ = 13,23', 'sujet', 'm')
text(ax, 11, y0 + ra*k/2, r'$r_a$ = 28,35', 'sujet', 'm', rot=90)
text(ax, 14 + r*k/2, y0 + ra*k + 3.5, '375', 'sujet', 'm')
text(ax, 38, y0 + 14, '×', 'encre', 'l')
box(ax, 50, y0, rb*k, rc*k, 'autre', r=0.5)
text(ax, 50 + rb*k/2, y0 - 3.5, r'$r_b$ = 39,69', 'autre', 'm')
text(ax, 47, y0 + rc*k/2, r'$r_c$ = 66,14', 'autre', 'm', rot=90)
text(ax, 50 + rb*k/2, y0 + rc*k/2, '2 625', 'autre', 'm')
text(ax, 44, 13, '375 × 2 625 = 984 375', 'resultat', 'm')
text(ax, 44, 6, 'Δ² = 992,2² = 984 375', 'resultat', 'm', weight='bold')
save(fig, '37-091')
