import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
L = 66.0
def group(y, title, full, part, lab_full, lab_part, lab_gap):
    text(ax, 4, y + 17, title, 'encre', 's', ha='left', weight='bold')
    box(ax, 4, y + 7, L, 7, 'sujet', label=lab_full, size='s', r=0.3)
    w = L * part / full
    box(ax, 4, y - 1, w, 7, 'varie', label=lab_part, size='s', r=0.3)
    box(ax, 4 + w, y - 1, L - w, 7, 'varie', fill=False, dash=True, r=0.3)
    text(ax, 4 + L + 2, y + 2.5, lab_gap, 'varie', 's', ha='left')
group(46, 'un facteur', 4316, 4000, '4 316 g', '4 000 g', '−316')
group(14, 'le produit', 375492, 348000, '375 492 g', '348 000 g', '−27 492')
text(ax, 44, 38.5, 'même proportion : plus de 7 %', 'encre', 's')
save(fig, '10-087')
