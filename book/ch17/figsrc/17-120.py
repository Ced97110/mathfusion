import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 2, 66, 'Taxi : distance en km', 'fixe', 's', ha='left')
y1, y2 = 46, 20
for y in (y1, y2):
    f = numberline(ax, 12, 62, y, 0, 8, labels=False, arrow_right=True)
    text(ax, f(0), y - 4.5, '0', 'encre', 's'); text(ax, f(6), y - 4.5, '6', 'encre', 's')
text(ax, 2, y1 + 11, r'prix $= 15$ €', 'autre', 'm', ha='left')
ax.add_patch(Circle((f(6), y1), 1.6, ec=COL['autre'], fc=COL['autre'], zorder=4))
text(ax, 80, y1 + 5, 'un point', 'autre', 's', ha='right')
text(ax, 2, y2 + 11, r'prix $\leq 15$ €', 'sujet', 'm', ha='left')
line(ax, [(f(0), y2), (f(6), y2)], 'sujet', lw=3.0)
for v in (0, 6): ax.add_patch(Circle((f(v), y2), 1.6, ec=COL['sujet'], fc=COL['sujet'], zorder=4))
text(ax, 80, y2 + 5, 'une région', 'sujet', 's', ha='right')
save(fig, '17-120')
