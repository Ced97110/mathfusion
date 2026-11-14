import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
panels = [
    (22, 'limite', 'reste ordinaire', r'$f_{j-1}(c)=+f_{j+1}(c)$', ['−   +   −', '−   −   −'], ['2 changements', '0 changement'], 'le compte varie'),
    (66, 'resultat', 'signe renversé', r'$f_{j-1}(c)=-f_{j+1}(c)$', ['−   +   +', '−   −   +'], ['1 changement', '1 changement'], 'le compte reste 1'),
]
for cx, role, head, rel, rows, counts, concl in panels:
    text(ax, cx, 61, head, role, 'm', weight='bold')
    text(ax, cx, 54, rel, 'encre', 's')
    for k, y in enumerate((38, 20)):
        box(ax, cx - 13, y, 26, 9, role, label=rows[k], size='m')
        text(ax, cx, y - 4, counts[k], 'encre', 's')
    text(ax, cx, 6, concl, role, 'm')
save(fig, '69-097')
