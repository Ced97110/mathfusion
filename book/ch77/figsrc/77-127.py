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
text(ax, 8, 50, r'polynôme minimal : degré 2', 'sujet', 's', ha='left')
box(ax, 8, 36, 24, 10, 'sujet', label=r'$\lambda^2-2$')
text(ax, 8, 28, r'caractéristique : degré 4', 'varie', 's', ha='left')
box(ax, 8, 14, 24, 10, 'varie', label=r'$\lambda^2-2$'); box(ax, 34, 14, 24, 10, 'varie', label=r'$\lambda^2-2$')
brace(ax, 8, 58, 13, 'varie', label=r'$(\lambda^2-2)^2$')
text(ax, 73, 33, r'$\neq$', 'limite', 'xl', weight='bold'); text(ax, 73, 25, 'différents', 'limite', 's')
save(fig, '77-127')
