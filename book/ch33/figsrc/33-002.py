import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 22
f = numberline(ax, 8, 78, y, 0, 0.12, step=0.02, arrow_right=False, every=2)
# zone below the limit
ax.add_patch(Rectangle((f(0), y + 0.6), f(0.0875) - f(0), 2.4, fc=FILL['resultat'], ec=COL['resultat'], lw=0.6, zorder=2))
ax.add_patch(Rectangle((f(0.0875), y + 0.6), f(0.12) - f(0.0875), 2.4, fc=FILL['limite'], ec=COL['limite'], lw=0.6, zorder=2))
text(ax, 25, y + 6, 'angle < 5°', 'resultat')
text(ax, 72, y + 6, 'angle > 5°', 'limite', 's')
line(ax, [(f(0.0875), y - 1.5), (f(0.0875), y + 16)], 'fixe', dash=True)
text(ax, f(0.0875), y + 19, r'$\tan\,5° \approx 0{,}0875$', 'fixe')
disc(ax, f(0.0833), y, 1.2, 'resultat')
arrow(ax, (f(0.0833) - 4, y + 10), (f(0.0833) - 0.8, y + 1.8), 'resultat')
text(ax, f(0.0833) - 17, y + 12, 'montée 0,5 m : 0,0833', 'resultat', 's')
disc(ax, f(0.1), y, 1.2, 'limite')
arrow(ax, (f(0.1), y - 11), (f(0.1), y - 1.8), 'limite')
text(ax, 60, y - 14, 'montée 0,6 m : 0,1 ≈ 5,7°', 'limite', 's')
save(fig, '33-002')
