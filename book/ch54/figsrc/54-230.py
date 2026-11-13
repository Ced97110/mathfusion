import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 31, 52, r'$(\mathbb{Z}/3)$', 'autre', 'xl')
text(ax, 56, 52, r'$[x]$', 'sujet', 'xl')
brace(ax, 18, 44, 46, 'autre', label='coefficients : 0, 1, 2', depth=1.8)
brace(ax, 50, 62, 46, 'sujet', label='polynômes en x', depth=1.8)
box(ax, 3, 4, 82, 32, 'sujet', fill=True)
text(ax, 44, 31, r'les éléments de $(\mathbb{Z}/3)[x]$', 'sujet', 's')
ex = [r'$x^2+2x+1$', r'$2x^3+x$', r'$x+2$', r'$2$']
pos = [(7, 17), (47, 17), (7, 7), (47, 7)]
wd = [38, 34, 38, 34]
for s, (x, y), w in zip(ex, pos, wd):
    box(ax, x, y, min(w, 37), 8, 'encre', label=s, size='s')
save(fig, '54-230')
