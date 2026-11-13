import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 15, 61, 'chapitre 1', 'limite', 's'); text(ax, 73, 61, 'entiers relatifs', 'resultat', 's')
rows = [('3 − 5', '−2'), ('10 − 20', '−10'), ('0 − 7', '−7')]
for i, (e, r) in enumerate(rows):
    y = 40 - i * 17
    box(ax, 2, y, 26, 11, 'limite', label='impossible', size='s')
    box(ax, 34, y, 20, 11, 'sujet', label=e, size='m')
    box(ax, 64, y, 22, 11, 'resultat', label=r, size='l')
    arrow(ax, (34, y + 5.5), (28, y + 5.5), 'limite'); arrow(ax, (54, y + 5.5), (64, y + 5.5), 'resultat')
save(fig, '13-120')
