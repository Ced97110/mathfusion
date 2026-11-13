import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
w, h, dx, dy = 15, 8, 16.5, 11
labs = ['(3, 0)', '(2, 1)', '(1, 2)', '(0, 3)', '0']
roles = ['sujet'] * 4 + ['resultat']
pos = [(3 + i * dx, 56 - i * dy) for i in range(5)]
for (x, y), lab, role in zip(pos, labs, roles):
    box(ax, x, y, w, h, role, label=lab, weight='bold' if lab == '0' else 'normal')
for i in range(4):
    (x0, y0), (x1, y1) = pos[i], pos[i + 1]
    arrow(ax, (x0 + w, y0 + h / 2), (x1 + w / 2, y1 + h), 'varie')
text(ax, 44, 67, 'chaque pas va plus bas', 'varie', 'm')
brace(ax, 3, 3 + 3 * dx + w, 50, 'sujet', label='quatre monômes', down=True) if False else None
brace(ax, 3, 3 + 3 * dx + w, 10, 'sujet', label='quatre monômes : au plus quatre pas', down=True, size='s')
save(fig, '55-101')
