import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
E=r'\varnothing'
nodes = {'0': (44, 28, r'$\varnothing$', 1), 'a': (18, 48, r'$\{a\}$', 1), 'b': (44, 48, r'$\{b\}$', 1), 'c': (70, 48, r'$\{c\}$', 0),
         'ab': (18, 68, r'$\{a,b\}$', 1), 'ac': (44, 68, r'$\{a,c\}$', 0), 'bc': (70, 68, r'$\{b,c\}$', 0), 'abc': (44, 88, r'$\{a,b,c\}$', 0)}
edges = (('0','a'),('0','b'),('0','c'),('a','ab'),('a','ac'),('b','ab'),('b','bc'),('c','ac'),('c','bc'),('ab','abc'),('ac','abc'),('bc','abc'))
bw, bh = 18, 9
for p, q in edges:
    (x1, y1, _, k1), (x2, y2, _, k2) = nodes[p], nodes[q]; both = k1 and k2
    if both: arrow(ax, (x2, y2), (x1, y1 + bh), 'sujet', lw=1.1)
    else: line(ax, [(x1, y1 + bh), (x2, y2)], 'fixe', lw=0.6, dash=True)
for k, (x, y, s, ink) in nodes.items():
    box(ax, x - bw / 2, y, bw, bh, 'sujet' if ink else 'fixe', fill=bool(ink), label=s, size='s', dash=not ink)
text(ax, 72, 90, r'sans $c$ : un idéal', 'sujet', 's')
arrow(ax, (6, 12), (6, 4), 'sujet', lw=1.1); text(ax, 9, 8, 'tout dessous est dedans', 'sujet', 's', ha='left')
box(ax, 52, 5, 8, 6, 'fixe', fill=False, dash=True, r=0.6); text(ax, 62, 8, 'contient $c$', 'fixe', 's', ha='left')
save(fig, '80-335')
