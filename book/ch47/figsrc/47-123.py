import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
for x, lab, role, cap in [(6, 's', 'varie', 'g⁻¹'), (34, 'r', 'sujet', 'n'), (62, 's', 'varie', 'g')]:
    box(ax, x, 48, 18, 12, role, label=lab, size='l')
    text(ax, x + 9, 65, cap, role, 'm')
arrow(ax, (61.5, 54), (52.5, 54), 'varie'); arrow(ax, (33.5, 54), (24.5, 54), 'varie')
box(ax, 4, 4, 80, 30, 'sujet', fill=False, dash=True)
text(ax, 8, 29, 'N : rotations', 'sujet', 's', ha='left')
for x, t, role in [(18, '1', 'fixe'), (34, 'r', 'sujet'), (50, 'r²', 'fixe'), (66, 'r³', 'resultat')]:
    disc(ax, x, 16, 5, role, label=t)
arrow(ax, (15, 47), (64, 21.5), 'resultat')
text(ax, 40, 40, '= r³', 'resultat', 'm')
save(fig, '47-123')
