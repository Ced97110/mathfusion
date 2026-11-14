import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
X = lambda c: 26 + c * 14
def tile(c, y, s, role):
    box(ax, X(c), y, 12, 9, role, label=s, size='s')
rows = [(56, 'varie', r'$\langle g\rangle$', [(0, '(0, 0)'), (2, '(2, 0)')]),
        (38, 'autre', r'K : $\mathbb{Z}/4$', [(0, '(0, 0)'), (1, r'$a$'), (2, '(2, 0)'), (3, r'$3a$')]),
        (20, 'autre', r'K : $\mathbb{Z}/2\oplus\mathbb{Z}/2$', [(0, '(0, 0)'), (1, '(0, 1)'), (2, '(2, 0)'), (3, '(2, 1)')])]
for y, role, lab, tiles in rows:
    text(ax, 23, y + 4.5, lab, role, 's', ha='right')
    for c, s in tiles:
        tile(c, y, s, 'limite' if s == '(2, 0)' else ('fixe' if s == '(0, 0)' else role))
for ya, yb in ((55.5, 47.5), (37.5, 29.5)):
    line(ax, [(X(2) + 6, ya), (X(2) + 6, yb)], 'limite', lw=0.9, dash=True)
text(ax, 44, 13, '(2, 0) est dans les trois', 'limite', 's')
text(ax, 44, 6, r'donc $K$ touche $\langle g\rangle$ : aucun complément', 'resultat', 's', weight='bold')
text(ax, 44, 69.5, r'$K$ : complément cherché, 4 éléments', 'encre', 's')
save(fig, '60-259')
