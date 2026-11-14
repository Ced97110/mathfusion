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

fig, ax = canvas(62)
x0, cw = 14, 22
cells = [[r'$1+\sqrt{2}+\sqrt{3}$', r'$1-\sqrt{2}+\sqrt{3}$'], [r'$1+\sqrt{2}-\sqrt{3}$', r'$1-\sqrt{2}-\sqrt{3}$']]
for r in range(2):
    yy = 34 - r * 12
    text(ax, 7, yy + 5.5, [r'$+\sqrt{3}$', r'$-\sqrt{3}$'][r], 'autre', 's')
    for c in range(2):
        box(ax, x0 + c * cw + 0.5, yy, cw - 1, 11, 'sujet', label=cells[r][c], size='s')
for c in range(2):
    text(ax, x0 + c * cw + cw / 2, 49, [r'$+\sqrt{2}$', r'$-\sqrt{2}$'][c], 'varie', 's')
    brace(ax, x0 + c * cw + 1, x0 + (c + 1) * cw - 1, 20.5, 'resultat', label=[r'$2\sqrt{2}$', r'$-2\sqrt{2}$'][c])
text(ax, 73, 36, r'somme $=4$', 'resultat', 'm', weight='bold')
text(ax, 73, 24, r'produit $=-8$', 'resultat', 'm', weight='bold')
save(fig, '77-122')
