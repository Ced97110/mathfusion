import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
assert 16 + 8 + 2 + 1 == 27 and 4 + 2 == 6 and 2 + 2 + 2 == 6
rows = [(52, '27 =', ['16', '8', '2', '1'], 'resultat', 'toutes différentes'),
        (32, '6 =', ['4', '2'], 'resultat', 'différentes'),
        (12, '6 =', ['2', '2', '2'], 'limite', 'la même, 3 fois')]
for y, lab, vals, role, note in rows:
    text(ax, 3, y + 6, lab, 'encre', 'm', ha='left')
    for i, v in enumerate(vals):
        box(ax, 18 + i * 16, y, 14, 12, role, label=v, size='l')
    text(ax, 18 + len(vals) * 16 + 1, y + 6, note, role, 's', ha='left') if len(vals) < 4 else text(ax, 44, y - 4, note, role, 's')
save(fig, '53-112')
