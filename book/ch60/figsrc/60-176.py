import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role='encre', size='m', cw=7.0, P=6.0, lw=0.9):
    r = len(rows); c = len(rows[0]); fs = SIZE[size]
    ls = ((P / (0.3387 * fs)) - 0.2) / 0.8
    for j in range(c):
        t = text(ax, cx + (j - (c - 1) / 2) * cw, cy, '\n'.join(rows[i][j] for i in range(r)), role, size); t.set_linespacing(ls)
    hw = c * cw / 2; hh = r * P / 2 + 0.4
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.2, cy - hh)], role, lw=lw)
fig, ax = canvas(74)
bx = (38, 63); bw = 23
text(ax, 20, 66, r'$f=(\lambda-2)^2$', 'sujet', 's')
for x in bx:
    box(ax, x, 61, bw, 10, 'sujet', label=r'$\lambda-2$', size='s')
mat(ax, 20, 42, [['2', '1'], ['0', '2']], 'autre', cw=6)
text(ax, 20, 32, r'$m=(\lambda-2)^2$', 'autre', 's')
for x in bx:
    box(ax, x, 37, bw, 10, 'autre', label=r'$\lambda-2$', size='s')
mat(ax, 20, 16, [['2', '0'], ['0', '2']], 'autre', cw=6)
text(ax, 20, 6, r'$m=\lambda-2$', 'autre', 's')
box(ax, bx[0], 11, bw, 10, 'autre', label=r'$\lambda-2$', size='s')
box(ax, bx[1], 11, bw, 10, 'autre', fill=False, dash=True)
text(ax, bx[1] + bw / 2, 16, 'absent', 'autre', 's')
save(fig, '60-176')
