import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
w, h, x0 = 14, 9, 24
def row(y, vals, role):
    for i, v in enumerate(vals):
        box(ax, x0 + i * w, y, w, h, role, label=v, size='s')
text(ax, 3, 64.5, r'$a$', 'sujet', 's', ha='left')
row(60, ['1,5', '2', '0'], 'sujet')
text(ax, 3, 52.5, r'$b$', 'autre', 's', ha='left')
row(48, ['0,5', '1', '3'], 'autre')
text(ax, 3, 40.5, r'$a+b$', 'resultat', 's', ha='left')
row(36, ['2', '3', '3'], 'resultat')
text(ax, 18, 56.5, '+', 'encre', 'l')
line(ax, [(x0, 45), (x0 + 3 * w, 45)], 'encre', lw=0.8)
for i in range(3):
    line(ax, [(x0 + i * w + w / 2, 60), (x0 + i * w + w / 2, 45)], 'fixe', lw=0.3, dash=True)
    line(ax, [(x0 + i * w + w / 2, 48), (x0 + i * w + w / 2, 45)], 'fixe', lw=0.3, dash=True)
arrow(ax, (x0 + 3 * w + 4, 64), (x0 + 3 * w + 4, 36), 'fixe', lw=0.6)
box(ax, 12, 8, 64, 14, 'varie', label=r'$2\times a$ : chaque case $\times\,2$' + '\n' + r'$(3\,;\,4\,;\,0)$', size='s')
save(fig, '58-097')
