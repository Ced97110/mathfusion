import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(54)
def table(x0, title, cells, total):
    text(ax, x0 + 20, 50, title, 'encre', 's')
    for k, (s, role) in enumerate(cells):
        r, c = divmod(k, 2)
        box(ax, x0 + c * 20.5, 30 - r * 14.5, 19.5, 13, role, s, 's')
    text(ax, x0 + 20, 9, total, 'resultat', 's')
table(2, r'$(1+i)(1+j)$', [(r'$1\cdot1=1$', 'fixe'), (r'$1\cdot j=j$', 'fixe'), (r'$i\cdot1=i$', 'fixe'), (r'$i\cdot j=k$', 'varie')], r'$1+i+j+k$')
table(47, r'$(1+j)(1+i)$', [(r'$1\cdot i=i$', 'fixe'), (r'$1\cdot1=1$', 'fixe'), (r'$j\cdot i=-k$', 'varie'), (r'$j\cdot1=j$', 'fixe')], r'$1+i+j-k$')
text(ax, 44.5, 22, '≠', 'limite', 'l', weight='bold')
text(ax, 44, 2.5, 'orange : seul ce produit change', 'varie', 's')
save(fig, '51-265')
