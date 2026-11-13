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

fig, ax = canvas(70)
items = [(56, r'$p=1+\sqrt{2}$', ['1','2'], ['1','1'], 'sujet', r'$=P$'),
         (36, '3', ['3','0'], ['0','3'], 'varie', r'$=3\cdot 1$'),
         (16, '1', ['1','0'], ['0','1'], 'fixe', r'$=1$')]
for y, lab, r1, r2, role, res in items:
    box(ax, 3, y - 5, 25, 10, role, label=lab)
    arrow(ax, (30, y), (38, y), 'varie')
    mat2(ax, 50, y, r1, r2, role)
    text(ax, 70, y, res, role, 'l')
save(fig, '77-116')
