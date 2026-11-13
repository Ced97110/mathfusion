import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
toks = [('5', 'sujet'), ('x', 'autre'), ('6', 'sujet'), ('b', 'autre'), ('8', 'sujet'), ('a', 'autre'), ('c', 'autre')]
nums = [i for i, t in enumerate(toks) if t[1] == 'sujet']
lets = sorted([i for i, t in enumerate(toks) if t[1] == 'autre'], key=lambda i: toks[i][0])
tx = lambda i: 5.5 + 11 * i
for i, (s, r) in enumerate(toks):
    box(ax, tx(i) - 4.5, 62, 9, 8, r, label=(s if r == 'sujet' else '$' + s + '$'))
box(ax, 3, 34, 40, 10, 'sujet', label='5 · 6 · 8 = 240')
box(ax, 45, 34, 40, 10, 'autre', label=r'$a\ b\ c\ x$')
for n, i in enumerate(nums): arrow(ax, (tx(i), 61.5), (10 + 13 * n, 44.5), 'varie', lw=0.7)
for n, i in enumerate(lets): arrow(ax, (tx(i), 61.5), (54 + 8.5 * n, 44.5), 'varie', lw=0.7)
box(ax, 20, 10, 48, 10, 'resultat', label=r'$240\,abcx$')
arrow(ax, (23, 33.5), (34, 20.5), 'varie'); arrow(ax, (65, 33.5), (54, 20.5), 'varie')
text(ax, 44, 4, 'même nombre qu’au départ', 'resultat', 's')
save(fig, '12-100')
