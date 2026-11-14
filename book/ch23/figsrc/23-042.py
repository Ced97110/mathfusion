import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for x, w_, t in ((3, 18, 'signe de k'), (23, 36, 'solutions'), (61, 24, 'exemple')):
    text(ax, x + w_ / 2, 62, t, 'fixe', 's')
rows = [(46, 'k > 0', r'deux : $\sqrt{k}$ et $-\sqrt{k}$', 'resultat', 'x² = 16 : 4, −4'),
        (32, 'k = 0', 'une : 0', 'resultat', 'x² = 0 : 0'),
        (18, 'k < 0', 'aucune', 'limite', 'x² = −16 : aucune')]
for y, a, b, r, e in rows:
    box(ax, 3, y, 18, 10, 'sujet', label=a)
    box(ax, 23, y, 36, 10, r, label=b, size='s')
    box(ax, 61, y, 24, 10, 'fixe', label=e, size='s')
save(fig, '23-042')
