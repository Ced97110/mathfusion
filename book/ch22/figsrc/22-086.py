import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(70)
fr(ax, 22, 54, r'$\sqrt{3}$', r'$\sqrt{5}$', 'sujet')
fr(ax, 66, 54, r'$\sqrt{15}$', r'$5$', 'autre')
text(ax, 22, 33, '≈ 1,732 / 2,236', 'sujet', 's')
text(ax, 66, 33, '≈ 3,873 / 5', 'autre', 's')
arrow(ax, (22, 29), (22, 22), 'sujet'); arrow(ax, (66, 29), (66, 22), 'autre')
box(ax, 8, 11, 28, 10, 'sujet', label='0,775')
box(ax, 52, 11, 28, 10, 'autre', label='0,775')
text(ax, 44, 16, '=', 'resultat', 'xl')
text(ax, 44, 54, '=', 'encre', 'xl')
text(ax, 22, 3, 'radical en bas', 'sujet', 's')
text(ax, 66, 3, 'radical en haut', 'autre', 's')
save(fig, '22-086')
