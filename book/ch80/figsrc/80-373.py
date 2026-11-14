import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'termes $n!/i!$, signes + − + −', 'fixe', 's')
for r, (n, terms, res) in enumerate([(3, ['+6', '−6', '+3', '−1'], 2), (4, ['+24', '−24', '+12', '−4', '+1'], 9)]):
    y = 34 - r * 22
    text(ax, 3, y + 5, r'$n=%d$' % n, 'encre', 'm', ha='left')
    for i, t in enumerate(terms): box(ax, 16 + i * 11.5, y, 10, 10, 'sujet' if t[0] == '+' else 'varie', label=t, size='s')
    text(ax, 80, y + 5, r'$=%d$' % res, 'resultat', 'l')
save(fig, '80-373')
