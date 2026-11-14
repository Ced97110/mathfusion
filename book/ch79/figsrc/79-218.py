import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def nb(ax, cx, cy, w, h, role, label, size="s"):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size)
fig, ax = canvas(88)
text(ax, 44, 84, r'axiomes sur $\vee$ et $\wedge$ seuls', 'encre', 'm', weight='bold')
text(ax, 44, 77, "aucun ordre n'est donné", 'fixe', 's')
def row(y, a, b, r, sym, name):
    nb(ax, 12, y, 16, 8, 'sujet', a, 'm'); nb(ax, 42, y, 16, 8, 'autre', b, 'm'); nb(ax, 70, y, 24, 11, 'resultat', r + '\n' + name, 's')
    text(ax, 27, y, sym, 'varie', 'l')
    arrow(ax, (51, y), (57.5, y), 'fixe', lw=0.9)
row(60, '{1}', '{2}', '{1, 2}', r'$\vee$', 'union')
row(38, '{1}', '{2}', '∅', r'$\wedge$', 'intersection')
nb(ax, 12, 14, 16, 8, 'sujet', '{1}', 'm'); nb(ax, 42, 14, 16, 8, 'autre', '{2}', 'm')
arrow(ax, (21, 14), (33, 14), 'varie', lw=1.0)
text(ax, 27, 7, 'complément', 'varie', 's')
save(fig, '79-218')
