import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(60)
fr(ax, 22, 28, r'$\sqrt{3}$', r'$\sqrt{5}$', 'fixe')
box(ax, 14, 20, 16, 8, 'varie', fill=False, lw=1.2)
text(ax, 22, 8, 'radical en bas', 'varie', 's')
text(ax, 44, 28, '=', 'encre', 'xl')
text(ax, 44, 38, 'même nombre', 'fixe', 's')
fr(ax, 66, 28, r'$\sqrt{15}$', r'$5$', 'sujet')
box(ax, 58, 20, 16, 8, 'resultat', fill=False, lw=1.2)
text(ax, 66, 8, 'entier en bas', 'resultat', 's')
text(ax, 66, 52, 'on préfère', 'resultat', 'm', weight='bold')
save(fig, '22-084')
