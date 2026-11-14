import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

EM = ' '
def pitch(size='m'):
    return 1.636 * SIZE[size] * 25.4 / 72
def rowstr(vals):
    return EM.join(vals)
def brk(ax, cx, cy, hw, hh, role='encre'):
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.3, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.3, cy - hh)], role, lw=0.8)
def mat2(ax, cx, cy, r1, r2, role='encre', size='m'):
    text(ax, cx, cy + 3.2, rowstr(r1), role, size); text(ax, cx, cy - 3.2, rowstr(r2), role, size)
    brk(ax, cx, cy, 4.8, 5.4, role)

fig, ax = canvas(56)
cx = 44; p = pitch()
for bx in (-1, 1):
    for by in (0, 1):
        box(ax, cx + bx * 4.33 - 4.1 if bx > 0 else cx - 4.33 - 4.1 + 0, 20.4 + by * 12 if False else 20.4 + by * 12, 8.2, 11.4, 'fixe', fill=False, dash=True, lw=0.5)
rows = [['1','2','3','0'], ['1','1','0','3'], ['1','0','1','2'], ['0','1','1','1']]
ys = [41, 35, 29, 23]
for i, rw in enumerate(rows):
    text(ax, cx, ys[i], rowstr(rw), 'encre', 'm')
    box(ax, cx + (i - 1.5) * p - 2.3, ys[i] - 2.8, 4.6, 5.6, 'resultat', fill=False, lw=1.0, r=0.5)
brk(ax, cx, 32, 10.5, 13.2)
text(ax, cx, 52, 'diagonale : 1, 1, 1, 1', 'resultat', 'm')
text(ax, cx, 9, r'$1+1+1+1=4$', 'resultat', 'l')
save(fig, '77-117')
