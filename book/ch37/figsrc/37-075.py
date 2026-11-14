import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
k, y0 = 1.1, 16
fig, ax = canvas(62)
w1, h1 = 35*k, math.sqrt(984375)/35*k
box(ax, 9, y0, w1, h1, 'sujet', r=0.5)
text(ax, 9 + w1/2, y0 + h1/2, 'Δ = 992,2', 'sujet', 'l')
text(ax, 9 + w1/2, y0 - 3.5, r'$s-a$ = 35', 'sujet', 'm')
text(ax, 5.5, y0 + h1/2, r'$r_a$ = 28,35', 'sujet', 'm', rot=90)
w2, h2 = 5*k, 8.66*k
box(ax, 60, y0, w2, h2, 'autre', r=0.4)
text(ax, 60 + w2/2, y0 - 3.5, r'$s-a$ = 5', 'autre', 'm')
text(ax, 60 + w2 + 2, y0 + h2/2, r'$r_a$ = 8,66', 'autre', 'm', ha='left')
text(ax, 60 + w2/2, y0 + h2 + 3.5, 'Δ = 43,30', 'autre', 'm')
text(ax, 28, y0 + h1 + 4, 'champ de 40, 50, 60', 'sujet', 'm')
text(ax, 70, y0 + h1 + 4, 'équilatéral de côté 10', 'autre', 'm')
text(ax, 44, y0 + h1 + 11, r'$\Delta = r_a\,(s-a)$', 'resultat', 'l')
save(fig, '37-075')
