import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(64)
text(ax, 44, 59, r'$(1+i)(1+j)$', 'encre', 's')
text(ax, 44, 5, r'$(1+j)(1+i)$', 'encre', 's')
xs = [12, 32, 52, 72]
top = ['1', r'$i$', r'$j$', r'$+k$']; bot = ['1', r'$i$', r'$j$', r'$-k$']
for k, x in enumerate(xs):
    role = 'varie' if k == 3 else 'fixe'
    box(ax, x - 8, 42, 16, 11, role, top[k], 'l')
    box(ax, x - 8, 11, 16, 11, role, bot[k], 'l')
    if k < 3: line(ax, [(x, 41), (x, 36.5)], 'fixe'); line(ax, [(x, 27.5), (x, 23)], 'fixe')
text(ax, 72, 32, r'$\neq$', 'varie', 'xl')
text(ax, 32, 32, 'trois termes égaux', 'fixe', 's')
text(ax, 72, 26.5, 'signe de k', 'varie', 's')
save(fig, '51-267')
