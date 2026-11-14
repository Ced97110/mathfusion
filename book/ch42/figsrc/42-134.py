import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def row(cx, items):
    n = len(items)
    for i, (lab, role, dash) in enumerate(items):
        x = cx + (i - (n - 1) / 2) * 9.5
        b = box(ax, x - 4, 38, 8, 8, role, label=lab, dash=dash)
cL, cR = 22, 66
text(ax, cL, 54, r'$A \setminus B$', 'sujet', 'l')
text(ax, cR, 54, r"$A \cap B'$", 'sujet', 'l')
row(cL, [('1', 'sujet', False), ('2', 'sujet', False), ('3', 'limite', False)])
row(cR, [('1', 'sujet', False), ('2', 'sujet', False), ('5', 'fixe', True), ('6', 'fixe', True)])
text(ax, cL, 31, 'on retire 3', 'limite', 's')
text(ax, cR, 31, 'on garde ceux de A', 'sujet', 's')
for cx in (cL, cR):
    arrow(ax, (cx, 27), (cx, 22), 'resultat')
    box(ax, cx - 8, 10, 16, 10, 'resultat', label='1 et 2')
text(ax, 44, 15, '=', 'resultat', 'l', weight='bold')
save(fig, '42-134')
