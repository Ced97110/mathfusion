import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 37, 58, '2', 'sujet', 'l', weight='bold', ha='right')
text(ax, 38, 58, ',35', 'fixe', 'l', weight='bold', ha='left')
w_ = 24
for i, x in enumerate((6, 32)):
    box(ax, x, 22, w_, w_, 'sujet', label='1 m')
box(ax, 58, 22, w_, w_, 'fixe', fill=False, dash=True)
ax.add_patch(Rectangle((58.8, 22.8), (w_ - 1.6) * 0.35, w_ - 1.6, ec='none', fc=FILL['fixe'], zorder=2))
text(ax, 70, 34, 'le reste', 'fixe', 's')
brace(ax, 6, 56, 20, 'sujet', '2 mètres entiers', down=True)
arrow(ax, (31, 54), (31, 49), 'sujet')
save(fig, '08-024')
