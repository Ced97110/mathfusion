import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, y0 = 8, 52
L = 70
poly(ax, [(x0, y0), (x0 + L, y0), (x0 + L, y0 + L / 12)], 'sujet')
text(ax, x0 + L / 2, y0 - 4, 'avance = côté adjacent', 'autre')
text(ax, x0 + L - 2, y0 + 11, 'montée = côté opposé', 'varie', ha='right')
box(ax, 4, 22, 38, 20, 'varie', label='')
text(ax, 23, 36, 'pente', 'varie')
text(ax, 23, 28, r'$0{,}5\ /\ 6 = 1/12$', 'varie')
box(ax, 46, 22, 38, 20, 'autre', label='')
text(ax, 65, 36, 'tangente', 'autre')
text(ax, 65, 28, r'$0{,}5\ /\ 6 = 1/12$', 'autre')
text(ax, 44, 32, '=', 'resultat', 'xl', weight='bold')
box(ax, 14, 2, 60, 9, 'resultat', label='un seul nombre : 1/12')
arrow(ax, (23, 21.5), (30, 11.6), 'resultat')
arrow(ax, (65, 21.5), (58, 11.6), 'resultat')
save(fig, '33-004')
