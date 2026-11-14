import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(60)
def row(y, sign, role, name):
    box(ax, 12, y, 54, 12, role, fill=True)
    text(ax, 24, y + 6, '4', role, 'l')
    box(ax, 33, y + 2, 9, 8, 'varie', label=sign, size='l')
    text(ax, 54, y + 6, r'$\sqrt{6}$', role, 'l')
    text(ax, 76, y + 6, name, role, 's')
row(40, '+', 'sujet', 'somme')
row(8, '−', 'autre', 'conjugué')
arrow(ax, (37.5, 38), (37.5, 22), 'varie')
text(ax, 55, 30, 'signe du milieu changé', 'varie', 's')
text(ax, 24, 30, 'même 4', 'fixe', 's')
save(fig, '22-089')
