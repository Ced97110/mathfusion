import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 8, 74, 32, 0, 12, arrow_right=False, size='s')
for v in range(13):
    if v % 2 == 0: disc(ax, f(v), 32, 1.5, 'sujet')
    else: disc(ax, f(v), 32, 1.2, 'fixe', fill=False)
for k in range(1, 6):
    arrow(ax, (f(2 * k - 2) + 1.6, 36), (f(2 * k) - 1.6, 36), 'varie', curve=-0.5, lw=0.7)
text(ax, 44, 55, r'$4a+6b$ : toujours pair', 'sujet', 'm')
text(ax, 44, 48, r'$2=6-4$ en fait partie', 'resultat', 's')
brace(ax, f(0), f(12), 24, 'sujet', label=r'tous les multiples de $2$', depth=2.0)
text(ax, 44, 8, 'un seul nombre engendre tout', 'encre', 's')
save(fig, '59-013')
