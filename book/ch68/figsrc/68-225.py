import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
labs = ['centre', '1 erreur', '2 erreurs', 'total']
nums = ['1', '90', '4005', '4096']
roles = ['sujet', 'sujet', 'sujet', 'resultat']
for i in range(4):
    x = 5 + i * 21
    text(ax, x + 7.5, 62, labs[i], 'fixe', 's')
    box(ax, x, 49, 15, 9, roles[i], label=nums[i], size='m')
for i, s in enumerate(['+', '+', '=']):
    text(ax, 5 + i * 21 + 18, 53.5, s, 'encre', 'l')
text(ax, 5 + 3 * 21 + 7.5, 43, r'$= 2^{12}$', 'resultat', 'm')
f = numberline(ax, 12, 72, 12, 0, 5, arrow_right=False)
ax.add_patch(Rectangle((f(0), 16), f(2) - f(0), 7, fc=FILL['sujet'], ec=COL['sujet'], lw=0.8, zorder=2))
text(ax, (f(0) + f(2)) / 2, 19.5, r'$t = 2$', 'sujet', 's')
ax.add_patch(Rectangle((f(3), 16), f(5) - f(3), 7, fc=FILL['autre'], ec=COL['autre'], lw=0.8, zorder=2))
text(ax, (f(3) + f(5)) / 2, 19.5, r'$t = 2$', 'autre', 's')
text(ax, 75, 12, 'distance', 'fixe', 's', ha='left')
arrow(ax, (f(0), 28), (f(5), 28), 'varie', both=True)
text(ax, 42, 33, r'distance $2t+1 = 5$ : sans contact', 'varie', 's')
save(fig, '68-225')
