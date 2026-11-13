import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$c$ = 0,01 = $10^{-2}$', 'sujet', 'xl')
x0, w = 9, 0.7
for i in range(100):
    ax.add_patch(Rectangle((x0 + i * w, 22), w, 9, ec=COL['fixe'], fc=FILL['sujet'] if i == 0 else FILL['fixe'], lw=0.25, zorder=2))
for k in range(0, 11):
    line(ax, [(x0 + k * 7, 21), (x0 + k * 7, 32)], 'fixe', lw=0.6)
ax.add_patch(Rectangle((x0, 22), w, 9, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=3))
arrow(ax, (x0 + 0.35, 43), (x0 + 0.35, 33), 'sujet')
text(ax, x0 + 3, 46, '1 cm = 0,01 m', 'sujet', 's', ha='left')
brace(ax, x0, x0 + 70, 20, 'resultat', '1 m = 100 cm')
save(fig, '11-041')
