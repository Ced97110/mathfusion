import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, 'même écart : 2', 'resultat', 'l')
f = numberline(ax, 6, 70, 12, 0, 12)
for (a, b, y, name, c) in ((3, 5, 40, '(3, 5)', 'sujet'), (10, 12, 26, '(10, 12)', 'autre')):
    line(ax, [(f(a), y), (f(b), y)], c, lw=1.6)
    for v, r in ((a, c), (b, 'varie')):
        line(ax, [(f(v), y), (f(v), 13)], 'fixe', dash=True, lw=0.6)
        disc(ax, f(v), y, 1.5, r)
    text(ax, (f(a) + f(b)) / 2, y + 4.5, name, c, 'm')
text(ax, 80, 40, 'j’ai 3, dois 5', 'sujet', 's', ha='right') if False else None
save(fig, '13-090')
