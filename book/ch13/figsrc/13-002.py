import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
box(ax, 14, 36, 36, 9, 'sujet', label='compte : 3 €')
box(ax, 14, 22, 60, 9, 'varie', label='paiement : 5 €')
line(ax, [(50, 36), (50, 7)], 'fixe', dash=True)
box(ax, 50, 7, 24, 9, 'limite', label='dette : 2 €')
text(ax, 31, 11.5, r'$5-3=2$', 'encre', 'l')
save(fig, '13-002')
