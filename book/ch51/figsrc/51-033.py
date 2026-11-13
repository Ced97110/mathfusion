import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cols = [('groupe commutatif', 'sujet', ['A1 associativité', 'A2 commutativité', 'A3 neutre 0', 'A4 opposé −a'], '4 règles'),
        ('monoïde', 'autre', ['M1 associativité', 'M2 neutre 1'], '2 règles'),
        ('distributivité', 'fixe', ['D1 à gauche', 'D2 à droite'], '2 règles')]
for i, (head, role, rules, cnt) in enumerate(cols):
    x = 1 + i * 29.5
    text(ax, x + 13.5, 72, head, role, 's', weight='bold')
    for j, r in enumerate(rules):
        box(ax, x, 56 - j * 10, 27, 8, role, label=r, size='s')
    text(ax, x + 13.5, 56 - (len(rules) - 1) * 10 - 5, cnt, role, 's')
save(fig, '51-033')
