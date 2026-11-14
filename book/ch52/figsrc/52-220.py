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

fig, ax = canvas(70)
for y, role, s in ((58, 'sujet', r'$3+2i+5j+7k$'), (38, 'varie', r'$3-2i-5j-7k$'), (18, 'resultat', r'$3+2i+5j+7k$')):
    box(ax, 6, y - 5, 48, 10, role, label=s, size='m')
arrow(ax, (40, 53), (40, 43.5), 'varie'); text(ax, 44, 48, 'conjuguer', 'varie', 's', ha='left')
arrow(ax, (40, 33), (40, 23.5), 'varie'); text(ax, 44, 28, 'conjuguer', 'varie', 's', ha='left')
text(ax, 58, 18, 'départ retrouvé', 'resultat', 's', ha='left')
text(ax, 58, 58, 'quaternion', 'sujet', 's', ha='left')
save(fig, '52-220')
