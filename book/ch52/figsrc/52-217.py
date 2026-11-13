import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, rows, role='sujet', c=6.5, fills=None, size='m'):
    n = len(rows); m = len(rows[0]); x0 = cx - m * c / 2; y0 = cy - n * c / 2
    for (i, j), r in (fills or {}).items():
        box(ax, x0 + j * c + 0.4, y0 + (n - 1 - i) * c + 0.4, c - 0.8, c - 0.8, r, r=0.3, lw=0.4)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            if v != '': text(ax, x0 + (j + .5) * c, y0 + (n - 1 - i + .5) * c, str(v), role, size)
    for sx, d in ((x0 - 0.8, 1), (x0 + m * c + 0.8, -1)):
        line(ax, [(sx + d * 1.4, y0 - 0.5), (sx, y0 - 0.5), (sx, y0 + n * c + 0.5), (sx + d * 1.4, y0 + n * c + 0.5)], role, lw=1.0)

def cross(ax, x, y, role='encre'):
    line(ax, [(x - 1.5, y - 1.5), (x + 1.5, y + 1.5)], role); line(ax, [(x - 1.5, y + 1.5), (x + 1.5, y - 1.5)], role)

def eq(ax, x, y, role='encre'):
    line(ax, [(x - 1.6, y + 0.9), (x + 1.6, y + 0.9)], role); line(ax, [(x - 1.6, y - 0.9), (x + 1.6, y - 0.9)], role)

fig, ax = canvas(100)
for y0, role, name in ((76, 'autre', 'anti-isomorphisme'), (44, 'sujet', 'anti-automorphisme'), (12, 'autre', 'involution')):
    box(ax, 2, y0, 84, 20, role); text(ax, 22, y0 + 10, name, role, 'm')
def dd(x, y, lab, role, r=5): disc(ax, x, y, r, role, label=lab, size='s')
dd(58, 86, r'$R$', 'sujet'); dd(78, 86, r"$R'$", 'autre'); arrow(ax, (63.4, 86), (72.6, 86), 'varie')
dd(58, 54, r'$R$', 'sujet'); dd(78, 54, r'$R$', 'sujet'); arrow(ax, (63.4, 54), (72.6, 54), 'varie')
dd(52, 22, r'$x$', 'sujet', 4); dd(66, 22, r"$x'$", 'varie', 4); dd(80, 22, r'$x$', 'sujet', 4)
arrow(ax, (56.4, 22), (61.6, 22), 'varie'); arrow(ax, (70.4, 22), (75.6, 22), 'varie')
text(ax, 44, 70, "cas particulier : $R'=R$", 'varie', 's')
text(ax, 44, 38, 'et : deux fois = départ', 'varie', 's')
save(fig, '52-217')
