import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
cw, ch = 11.5, 7
def mat(x0, y0, vals, roles):
    for k, (v, role) in enumerate(zip(vals, roles)):
        i, j = k % 2, k // 2
        x, y = x0 + i * cw, y0 + (1 - j) * ch
        if v is None: box(ax, x, y, cw, ch, 'fixe', fill=False, dash=True, lw=0.5)
        else: box(ax, x, y, cw, ch, role, label=v, size='s')
y0 = 16
mat(2, y0, ['0,866', '−0,5', '0,5', '0,866'], ['sujet'] * 4)
mat(30, y0, ['0,7071', '−0,7071', '0,7071', '0,7071'], ['autre'] * 4)
mat(59, y0, ['0,2588', None, '0,9659', None], ['resultat'] * 4)
box(ax, 1, y0 + ch - 0.8, 2 * cw + 2, ch + 1.6, 'varie', fill=False, dash=True, lw=1.0)
box(ax, 29, y0 - 0.8, cw + 2, 2 * ch + 1.6, 'varie', fill=False, dash=True, lw=1.0)
m = y0 + ch
line(ax, [(26.6, m - 1.3), (29.2, m + 1.3)]); line(ax, [(26.6, m + 1.3), (29.2, m - 1.3)])
line(ax, [(55, m - 1), (58, m - 1)]); line(ax, [(55, m + 1), (58, m + 1)])
for x, s, role in ((13.5, 'rotation 30°', 'sujet'), (41.5, 'rotation 45°', 'autre'), (70, 'rotation 75°', 'resultat')):
    text(ax, x, 35, s, role, 's')
text(ax, 44, 7, '30° puis 45° : 30° + 45° = 75°', 'encre', 's')
save(fig, '34-181')
