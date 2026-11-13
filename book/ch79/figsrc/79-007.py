import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def S(*c): return r'$\{' + ','.join(c) + r'\}$'
text(ax, 20, 56, 'divisibilité', 'sujet', 'm'); text(ax, 70, 56, 'inclusion', 'autre', 'm')
L = {'4': (20, 10), '12': (9, 28), '20': (31, 28), '60': (20, 46)}
for a, b in [('4','12'),('4','20'),('12','60'),('20','60')]:
    (x1, y1), (x2, y2) = L[a], L[b]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    line(ax, [(x1 + ux * 3.4, y1 + uy * 3.4), (x2 - ux * 3.4, y2 - uy * 3.4)], 'sujet', lw=1.2)
for k, (x, y) in L.items(): disc(ax, x, y, 3.4, 'sujet', label=k, size='s')
R = {'b': (70, 10, S('b')), 'ab': (60, 28, S('a', 'b')), 'bc': (80, 28, S('b', 'c')), 'abc': (70, 46, S('a', 'b', 'c'))}
w, h = 16, 7
for a, b in [('b','ab'),('b','bc'),('ab','abc'),('bc','abc')]:
    (x1, y1), (x2, y2) = R[a][:2], R[b][:2]; d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    line(ax, [(x1 + ux * 4.5, y1 + uy * 4.5), (x2 - ux * 4.5, y2 - uy * 4.5)], 'autre', lw=1.2)
for k, (x, y, s) in R.items(): box(ax, x - w / 2, y - h / 2, w, h, 'autre', label=s, size='s')
text(ax, 44, 28, 'même forme', 'resultat', 's') if False else None
save(fig, '79-007')
