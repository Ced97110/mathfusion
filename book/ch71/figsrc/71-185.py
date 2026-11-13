import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
data = [(40, 'base 1', 'sujet', ['5', '16/5']), (24, 'base 2', 'autre', ['16', '4'])]
for y, lab, role, vals in data:
    text(ax, 2, y + 5, lab, role, 's', ha='left')
    for i, v in enumerate(vals):
        box(ax, 22 + i * 19, y, 16, 10, role, label=v)
text(ax, 2, 11, 'base 3 ?', 'limite', 's', ha='left')
for i, v in enumerate(['+', '−']):
    box(ax, 22 + i * 19, 6, 16, 10, 'limite', label=v, size='l', dash=True)
box(ax, 64, 24, 22, 26, 'resultat', label='$p=2$', size='l')
box(ax, 64, 6, 22, 10, 'limite', label='impossible', size='s', dash=True)
save(fig, '71-185')
