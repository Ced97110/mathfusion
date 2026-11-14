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

fig, ax = canvas(52)
for x, y, l, r in [(4, 27.5, r'$p$', 'sujet'), (14, 27.5, '3', 'varie'), (4, 17.5, '1', 'fixe'), (14, 17.5, r'$p$', 'sujet')]:
    box(ax, x, y, 9, 9, r, label=l, size='l')
brace(ax, 4, 23, 16.5, 'fixe', label=r'petite : 2×2')
arrow(ax, (26, 27), (38, 27), 'varie')
for x, y, l, r in [(40, 26, r'$P$', 'sujet'), (56, 26, r'$3\cdot 1$', 'varie'), (40, 12, '1', 'fixe'), (56, 12, r'$P$', 'sujet')]:
    box(ax, x, y, 15.5, 13.5, r, label=l, size='l')
brace(ax, 40, 71.5, 11, 'fixe', label=r'grande : 4×4')
brace(ax, 40, 55.5, 40, 'sujet', label=r'bloc 2×2', down=False)
save(fig, '77-115')
