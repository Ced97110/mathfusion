import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 8, 48, 30, 10, 'sujet', label=r'$a$ : 2 + 4'); box(ax, 50, 48, 30, 10, 'autre', label=r'$b$ : 6')
text(ax, 44, 53, '=', 'resultat', 'l')
text(ax, 44, 63, r'$c$ = 5', 'varie', 'm')
for cx, op, v, sg in ((22, '+', '11', 1), (66, '-', '1', -1)):
    arrow(ax, (cx, 46), (cx, 34), 'varie')
    text(ax, cx + 2, 40, r'$%s\,c$' % op, 'varie', 's', ha='left')
    box(ax, cx - 20, 20, 16, 12, 'sujet', label=r'$a%sc$ : %s' % (op, v), size='s')
    box(ax, cx + 4, 20, 16, 12, 'autre', label=r'$b%sc$ : %s' % (op, v), size='s')
    text(ax, cx, 26, '=', 'resultat', 'l')
text(ax, 44, 8, 'les deux côtés restent égaux', 'resultat', 's')
save(fig, '16-050')
