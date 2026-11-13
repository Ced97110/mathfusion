import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def tree(t, xs):
    # returns (x, depth, children drawn) ; leaves are strings
    if isinstance(t, str): return xs[t], 0, 0
def build(t, pos, y0, dy, bx):
    if isinstance(t, str):
        x = bx + pos.index(t) * 3.6; return x, y0 - 3 * dy * 0 - (MAXD) * dy + 0, 0
trees = [((('a','b'),'c'),'d'), (('a',('b','c')),'d'), (('a','b'),('c','d')), ('a',(('b','c'),'d')), ('a',('b',('c','d')))]
expr = [r'$((ab)c)d$', r'$(a(bc))d$', r'$(ab)(cd)$', r'$a((bc)d)$', r'$a(b(cd))$']
def depth(t): return 0 if isinstance(t, str) else 1 + max(depth(t[0]), depth(t[1]))
def draw(t, bx, ytop, dy, dx, cnt):
    if isinstance(t, str):
        i = cnt[0]; cnt[0] += 1; return bx + i * dx, ytop - 3 * dy
    (x1, y1), (x2, y2) = draw(t[0], bx, ytop, dy, dx, cnt), draw(t[1], bx, ytop, dy, dx, cnt)
    d = depth(t); y = ytop - (3 - d) * dy; x = (x1 + x2) / 2
    line(ax, [(x1, y1), (x1, y), (x2, y), (x2, y2)], 'sujet', lw=0.9); 
    return x, y
for k, t in enumerate(trees):
    bx = 6 + k * 17; draw(t, bx, 40, 6, 3.6, [0])
    for i in range(4): disc(ax, bx + i * 3.6, 22, 1.0, 'sujet')
    text(ax, bx + 5.4, 16, expr[k], 'encre', 's')
text(ax, 44, 47, '4 éléments : 5 placements', 'sujet', 'm', weight='bold')
save(fig, '45-099')
