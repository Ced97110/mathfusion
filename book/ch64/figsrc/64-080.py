import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(95)
cy = 63
disc(ax, 31, cy, 24, 'sujet', fill=False, lw=1.2)
disc(ax, 57, cy, 24, 'autre', fill=False, lw=1.2)
text(ax, 27, cy + 29.5, r'termes normaux dans $G$', 'sujet', 's')
text(ax, 63, cy + 29.5, 'facteurs simples', 'autre', 's')
text(ax, 19, cy, 'normale', 'sujet', 's')
text(ax, 69, cy, 'composition', 'autre', 's')
text(ax, 44, cy, 'principale', 'resultat', 's', weight='bold')
# tableau à deux cases à cocher
cols = (54, 76)
text(ax, cols[0], 28, r'normal dans $G$', 'sujet', 's')
text(ax, cols[1] + 2, 28, 'facteurs simples', 'autre', 's')
def yes(x, y): line(ax, [(x - 1.8, y), (x - 0.6, y - 1.6), (x + 2.0, y + 2.0)], 'resultat', lw=1.6)
def no(x, y):
    line(ax, [(x - 1.7, y - 1.7), (x + 1.7, y + 1.7)], 'limite', lw=1.6)
    line(ax, [(x - 1.7, y + 1.7), (x + 1.7, y - 1.7)], 'limite', lw=1.6)
rows = [('24, 12, 4, 2, 1', 'autre', 18, (False, True)),
        (r'composition de $\mathbb{Z}/60$', 'resultat', 7, (True, True))]
for lab, role, y, (a, b) in rows:
    text(ax, 2, y, lab, role, 's', ha='left')
    (yes if a else no)(cols[0], y)
    (yes if b else no)(cols[1] + 2, y)
save(fig, '64-080')
