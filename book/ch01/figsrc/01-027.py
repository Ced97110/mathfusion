import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
box(ax, 4, 26, 16, 16, 'sujet', label='0', size='l', weight='bold')
text(ax, 12, 46, 'zéro', 'sujet', 'm')
text(ax, 3, 20, 'ne dit pas « rien »', 'limite', 's', ha='left')
f = numberline(ax, 34, 78, 14, 0, 5)
disc(ax, f(0), 14, 1.6, 'sujet'); ax.patches[-1].set_zorder(3.5)
text(ax, 34, 6, 'point de départ', 'sujet', 's')
line(ax, [(20, 30), (34, 15.6)], 'sujet', dash=True)
for k in range(5):
    arrow(ax, (f(k), 15.5), (f(k + 1), 15.5), 'varie', curve=-0.5)
text(ax, 56, 26, 'des pas depuis 0', 'varie', 's')
save(fig, '01-027')
