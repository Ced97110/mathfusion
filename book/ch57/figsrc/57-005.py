import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
box(ax, 1.5, 9, 85, 30, 'fixe', fill=False, dash=True)
text(ax, 6, 35, 'ℤ²', 'sujet', 'l', ha='left', weight='bold')
text(ax, 80, 35, 'la boîte', 'fixe', 's', ha='right')
cw, ch, cy = 18, 12, 17
for x, lab, role in [(7, '(2, 1)', 'sujet'), (35, '(6, 3)', 'sujet'), (65, '(8, 4)', 'resultat')]:
    box(ax, x, cy, cw, ch, role, label=lab)
text(ax, 29, cy + ch / 2, '+', 'varie', 'xl', weight='bold')
text(ax, 58.5, cy + ch / 2, '=', 'varie', 'xl', weight='bold')
text(ax, 44, 5, '2 + 6 = 8   et   1 + 3 = 4', 'encre', 's')
save(fig, '57-005')
