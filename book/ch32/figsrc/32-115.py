import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
xs = [(4, 24, 'cos² x'), (31, 26, '− sin x'), (60, 24, '− 1')]
vals = ['0', '1', '−1']
for (x, w, s), v in zip(xs, vals):
    box(ax, x, 62, w, 11, 'fixe', label=s)
    arrow(ax, (x + w/2, 62), (x + w/2, 47))
    box(ax, x, 36, w, 11, 'sujet', label=v)
text(ax, 20, 54.5, 'x = 270°', 'varie', 's', ha='left')
brace(ax, 4, 84, 34, 'fixe')
arrow(ax, (44, 31), (44, 22))
box(ax, 14, 8, 60, 14, 'resultat', label='0 + 1 − 1 = 0 : vrai')
save(fig, '32-115')
