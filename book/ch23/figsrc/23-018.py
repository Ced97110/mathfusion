import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def row(ax, y, items, x0=None, h=8, gap=2, size='m'):
    tot = sum(it[2] for it in items) + gap * (len(items) - 1)
    x = (W - tot) / 2 if x0 is None else x0
    out = []
    for it in items:
        lab, role, w = it[0], it[1], it[2]
        dash = len(it) > 3 and it[3]
        sz = it[4] if len(it) > 4 else size
        box(ax, x, y, w, h, role, True, lab, sz, dash=dash)
        out.append((x + w / 2, x, w)); x += w + gap
    return out

fig, ax = canvas(62)
x0, y0, c = 6, 12, 5
for i in range(6):
    for j in range(6):
        poly(ax, [(x0+i*c, y0+j*c), (x0+(i+1)*c, y0+j*c), (x0+(i+1)*c, y0+(j+1)*c), (x0+i*c, y0+(j+1)*c)], 'sujet')
text(ax, x0 + 15, y0 + 33, '6', 'sujet', 's')
text(ax, x0 - 3, y0 + 15, '6', 'sujet', 's')
text(ax, x0 + 15, 6, 'aire 6 × 6 = 36', 'sujet', 's')
box(ax, 46, 40, 38, 9, 'sujet', True, r'$x^2=x\times x$')
box(ax, 46, 26, 38, 9, 'resultat', True, r'$x=6$ : $x^2$ vaut 36', 's')
box(ax, 46, 12, 38, 9, 'limite', True, r'non : $2\times x$ vaut 12', 's')
save(fig, '23-018')
