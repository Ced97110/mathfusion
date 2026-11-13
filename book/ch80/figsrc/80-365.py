import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0, u, y, h = 6, 5, 28, 10
segs = [(8, 'sujet', r'$\{2\}$'), (4, 'varie', r'$\{2,3\}$'), (2, 'varie', r'$\{2,5\}$'), (1, 'varie', r'$\{2,3,5\}$')]
x = x0; cs = []
for n, role, s in segs:
    box(ax, x, y, n * u, h, role, label=str(n), size='m'); cs.append(x + n * u / 2); x += n * u
brace(ax, x0, x0 + 75, y + h, 'resultat', label=r'$g(\{2\})=15$ : au moins 2', down=False)
brace(ax, x0, x0 + 40, y, 'sujet', label=r'$f(\{2\})=8$ : exactement 2', down=True)
text(ax, cs[0], 19, segs[0][2], 'sujet', 's'); text(ax, cs[1], 19, segs[1][2], 'varie', 's'); text(ax, cs[2], 19, segs[2][2], 'varie', 's')
line(ax, [(cs[3], y), (cs[3], 11)], 'varie'); text(ax, cs[3], 8, segs[3][2], 'varie', 's')
save(fig, '80-365')
