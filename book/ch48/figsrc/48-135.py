import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx = [14, 44, 74]; roles = ['sujet', 'autre', 'resultat']
mats = ['1   2\n0   1', '3   0\n0   2', '3   4\n0   2']; names = ['A', 'B', 'AB']; dets = ['1', '6', '6']
for c, m, r, nm, d in zip(cx, mats, roles, names, dets):
    box(ax, c - 11, 38, 22, 15, r); text(ax, c, 45.5, m, r, 'm'); text(ax, c, 56.5, nm, r, 'm')
    arrow(ax, (c, 38), (c, 25), 'varie'); box(ax, c - 11, 12, 22, 11, r, label='det = ' + d, size='m')
text(ax, 29, 45.5, '×', 'encre', 'l'); text(ax, 59, 45.5, '=', 'encre', 'l')
text(ax, 29, 17.5, '×', 'encre', 'l'); text(ax, 59, 17.5, '=', 'encre', 'l')
text(ax, 11, 33, 'det', 'varie', 's')
save(fig, '48-135')
