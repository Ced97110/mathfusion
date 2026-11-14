import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 30, 58, 'diviseurs élémentaires', 'sujet', 's')
text(ax, 62, 58, 'facteurs invariants', 'resultat', 's', ha='left')
text(ax, 30, 3.5, 'orange : plus grand de chaque premier', 'varie', 's')
rows = [([2, 2, 3, 3, 3, 5], {1, 4, 5}, 42), ([2, 3, 3], {0, 2}, 26), ([3], {0}, 10)]
for vals, pick, y in rows:
    for i, v in enumerate(vals):
        box(ax, 3 + i * 9.5, y, 8, 9, 'varie' if i in pick else 'sujet', label=str(v))
res = [r'$d_3=2\times3\times5=30$', r'$d_2=2\times3=6$', r'$d_1=3$']
ends = [58.5, 30.0, 11.0]
for k, (s, e) in enumerate(zip(res, ends)):
    y = rows[k][2] + 4.5
    if k > 0: arrow(ax, (e + 2, y), (60, y), 'fixe')
    text(ax, 62, y, s, 'resultat', 's', ha='left')
save(fig, '60-240')
