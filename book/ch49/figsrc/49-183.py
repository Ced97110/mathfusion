import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
spec = [('fixe', None), ('fixe', None), ('sujet', r'$y_1$'), ('sujet', r'$y_2$'), ('sujet', r'$y_3$')]
sizes = [1, 1, 2, 2, 2]; d = 4.4; pad = 1.6; gap = 4
ws = [n * d + 2 * pad for n in sizes]; x = (W - sum(ws) - 4 * gap) / 2; y = 30; starts = []
for k, (role, lab) in enumerate(spec):
    starts.append(x)
    box(ax, x, y - 4.5, ws[k], 9, role, dash=(lab is None))
    for i in range(sizes[k]):
        disc(ax, x + pad + d / 2 + i * d, y, 1.5, 'varie' if (lab and i == 0) else role)
    if lab:
        cx = x + pad + d / 2
        arrow(ax, (cx, y - 15), (cx, y - 6), 'varie', lw=0.8)
        text(ax, cx, y - 18, lab, 'varie', 'm', weight='bold')
    x += ws[k] + gap
brace(ax, starts[0], starts[1] + ws[1], y + 8, 'fixe', None, down=False, depth=2)
text(ax, (starts[0] + starts[1] + ws[1]) / 2, y + 15, r'centre : {1, $r^2$}', 'fixe', 's')
xe = starts[4] + ws[4]
brace(ax, starts[2], xe, y + 8, 'sujet', None, down=False, depth=2)
text(ax, (starts[2] + xe) / 2, y + 15, r'$j$ = 1, 2, 3', 'sujet', 's')
text(ax, W / 2, 5, '1 représentant par classe de 2', 'varie', 'm')
save(fig, '49-183')
