import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = numberline(ax, 10, 66, 14, 0, 4, 1, role='sujet')
text(ax, 80, 14, 'g', 'sujet', 'xl', weight='bold')
for g in (1, 2, 4):
    line(ax, [(f(g), 15.5), (f(g), 25)], 'varie', dash=True); disc(ax, f(g), 27, 2, 'varie')
ax.add_patch(Circle((f(3), 27), 2.4, ec=COL['sujet'], fc='none', lw=0.9, ls='--', zorder=2))
text(ax, f(3), 27, 'g', 'sujet', 'm', weight='bold')
text(ax, 44, 39, 'les gallons se lisent ici', 'sujet', 's')
save(fig, '09-117')
