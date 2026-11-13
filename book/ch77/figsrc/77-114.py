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

fig, ax = canvas(54)
small = [(4, 32.5, r'$p$', 'sujet'), (14, 32.5, '3', 'varie'), (4, 22.5, '1', 'fixe'), (14, 22.5, r'$p$', 'sujet')]
for x, y, l, r in small:
    box(ax, x, y, 9, 9, r, label=l, size='l')
text(ax, 13.5, 47, r'cases dans $E$', 'encre', 's')
arrow(ax, (25, 32), (37, 32), 'varie')
cx = 62; p = pitch()
blocks = [(-1, 1, 'sujet'), (1, 1, 'varie'), (-1, 0, 'fixe'), (1, 0, 'sujet')]
for bx, by, r in blocks:
    box(ax, cx + bx * 4.33 - 4.1, 20.4 + by * 12, 8.2, 11.4, r)
rows = [['1','2','3','0'], ['1','1','0','3'], ['1','0','1','2'], ['0','1','1','1']]
for i, rw in enumerate(rows):
    text(ax, cx, 41 - 6 * i, rowstr(rw), 'encre', 'm')
brk(ax, cx, 32, 10.5, 13.2)
text(ax, cx, 48, 'cases rationnelles', 'encre', 's')
save(fig, '77-114')
