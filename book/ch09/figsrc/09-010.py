import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u, y0 = 5, 8
box(ax, 8, y0, 10, 3 * u, 'sujet', r=0.3); box(ax, 22, y0, 10, 5 * u, 'varie', r=0.3)
for p in range(1, 5): line(ax, [(22, y0 + p * u), (32, y0 + p * u)], 'encre', lw=0.8)
line(ax, [(18, y0 + 3 * u), (32, y0 + 3 * u)], 'sujet', dash=True)
text(ax, 13, y0 + 3 * u + 3, r'$a=3$', 'sujet', 's'); text(ax, 27, y0 + 5 * u + 3, r'$b=5$', 'varie', 's')
text(ax, 38, 40, 'bleu pour orange', 'sujet', 's', ha='left')
text(ax, 38, 34, '3/5 = 0,6', 'resultat', 'l', ha='left', weight='bold')
text(ax, 38, 22, 'orange pour bleu', 'varie', 's', ha='left')
text(ax, 38, 16, '5/3 > 1', 'autre', 'l', ha='left', weight='bold')
save(fig, '09-010')
