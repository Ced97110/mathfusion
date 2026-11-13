import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [43, 60, 77]
for x, h in zip(cx, ['chaîne', 'primalité', 'factoriel']):
    text(ax, x, 59, h, 'sujet', 's', weight='bold')
rows = [(38, 'ℤ', ['vrai', 'vrai', 'vrai']), (20, 'ℤ[√−5]', ['vrai', 'faux', 'faux'])]
for y, name, vals in rows:
    text(ax, 3, y + 5, name, 'encre', 'm', ha='left')
    for x, v in zip(cx, vals):
        ok = v == 'vrai'
        box(ax, x - 8, y, 16, 10, 'resultat' if ok else 'limite', label=v, size='s')
text(ax, 44, 8, '2 : irréductible, non premier', 'limite', 's')
save(fig, '56-071')
