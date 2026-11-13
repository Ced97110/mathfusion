import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 80, 32, 0, 1, step=0.25, labels=False, arrow_right=False, tick=2.2)
for v, t in ((0, '0'), (0.25, '1/4'), (0.5, '1/2'), (0.75, '3/4'), (1, '1')):
    text(ax, f(v), 38, t, 'resultat' if v == 0.25 else 'fixe', 's')
ax.plot([f(0.25)] * 2, [29.8, 34.2], color=COL['resultat'], lw=1.6, zorder=2)
disc(ax, f(0.3), 32, 1.4, 'sujet')
text(ax, f(0.3), 49, '3/10', 'sujet', 'm'); arrow(ax, (f(0.3), 47), (f(0.3), 34), 'sujet')
brace(ax, f(0.25), f(0.3), 29, 'resultat', label='1/20')
brace(ax, f(0.3), f(0.5), 29, 'fixe', label='1/5')
text(ax, 44, 12, '3/10 devient 1/4 : le plus proche', 'resultat', 'm')
save(fig, '10-064')
