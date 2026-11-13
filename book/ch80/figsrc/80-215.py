import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
bw, bh = 14, 8
pos = {'0': (44, 12), '1': (22, 36), '2': (44, 36), '3': (66, 36), '12': (22, 60), '13': (44, 60), '23': (66, 60), '123': (44, 82)}
def lab(k): return r'$\varnothing$' if k == '0' else r'$\{' + ','.join(k) + r'\}$'
edges = [('0','1'),('0','2'),('0','3'),('1','12'),('1','13'),('2','12'),('2','23'),('3','13'),('3','23'),('12','123'),('13','123'),('23','123')]
for a, b in edges:
    (x1, y1), (x2, y2) = pos[a], pos[b]
    hot = (a, b) in (('0', '1'), ('1', '12'))
    line(ax, [(x1 + (x2 - x1) * 0.0, y1 + bh / 2), (x2, y2 - bh / 2)] if True else None, 'varie' if hot else 'fixe', lw=1.6 if hot else 0.8)
for k, (x, y) in pos.items():
    atom = k in ('1', '2', '3')
    box(ax, x - bw / 2, y - bh / 2, bw, bh, 'sujet' if atom else ('varie' if k == '12' else 'fixe'), label=lab(k), size='s')
text(ax, 2, 36, 'atomes', 'sujet', 's', ha='left')
text(ax, 2, 86, 'parties de $\\{1,2,3\\}$'.replace('parties de ', 'parties : '), 'fixe', 's', ha='left')
text(ax, 44, 3, r'$\{1\}$ est entre $\varnothing$ et $\{1,2\}$', 'varie', 's')
save(fig, '80-215')
