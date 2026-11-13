import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 2, 62, '24 €, un billet = 6 €', 'fixe', 's', ha='left')
y1, y2 = 42, 16
for y in (y1, y2):
    f = numberline(ax, 12, 60, y, 0, 4, arrow_right=True)
text(ax, 78, y1 - 7, 'billets', 'fixe', 's', ha='right')
text(ax, 2, y1 + 8, r'$6b = 24$', 'autre', 'm', ha='left')
ax.add_patch(Circle((f(4), y1), 1.6, ec=COL['autre'], fc=COL['autre'], zorder=4))
text(ax, 78, y1 + 6, 'seulement 4', 'autre', 's', ha='right')
text(ax, 2, y2 + 8, r'$6b \leq 24$', 'sujet', 'm', ha='left')
line(ax, [(f(0), y2), (f(4), y2)], 'sujet', lw=2.6)
for v in (1, 2, 3, 4): ax.add_patch(Circle((f(v), y2), 1.6, ec=COL['sujet'], fc=COL['sujet'], zorder=4))
text(ax, f(3), y2 + 5, '18 €', 'sujet', 's'); text(ax, f(4), y2 + 5, '24 €', 'sujet', 's')
save(fig, '17-125')
