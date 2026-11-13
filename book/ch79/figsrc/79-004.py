import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X = [18, 44, 70]; Y = [8, 24, 40, 56]; w, h = 15, 7
def S(*c): return r'$\{' + ','.join(c) + r'\}$'
nodes = {'o': (44, Y[0], r'$\emptyset$', 'fixe'), 'a': (X[0], Y[1], S('a'), 'fixe'), 'b': (X[1], Y[1], S('b'), 'fixe'), 'c': (X[2], Y[1], S('c'), 'fixe'),
         'ab': (X[0], Y[2], S('a', 'b'), 'sujet'), 'ac': (X[1], Y[2], S('a', 'c'), 'fixe'), 'bc': (X[2], Y[2], S('b', 'c'), 'autre'),
         't': (44, Y[3], S('a', 'b', 'c'), 'fixe')}
for lo, hi in [('o','a'),('o','b'),('o','c'),('a','ab'),('a','ac'),('b','ab'),('b','bc'),('c','ac'),('c','bc'),('ab','t'),('ac','t'),('bc','t')]:
    line(ax, [(nodes[lo][0], nodes[lo][1] + h / 2), (nodes[hi][0], nodes[hi][1] - h / 2)], 'fixe')
for k, (x, y, s, r) in nodes.items(): box(ax, x - w / 2, y - h / 2, w, h, r, label=s, size='s')
text(ax, 44, 3, '', 'fixe', 's') if False else None
text(ax, 44, 64, r'$\{a,b\}$ et $\{b,c\}$ incomparables', 'limite', 'm')
save(fig, '79-004')
