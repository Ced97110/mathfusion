import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 80, r'$\binom{4}{2}=\dfrac{4!}{2!\times 2!}$', 'sujet', 'l')
text(ax, 24, 70, '4! = 4×3×2×1 = 24', 'varie', 's')
arrow(ax, (41, 77.5), (26, 72.5), 'varie')
arrow(ax, (24, 67.5), (24, 54), 'varie')
text(ax, 64, 70, '2! × 2! = 2 × 2 = 4', 'varie', 's')
arrow(ax, (55, 77.5), (62, 72.5), 'varie')
arrow(ax, (64, 67.5), (60.5, 54), 'varie')
for x0 in [12.5, 23.5, 34.5, 45.5, 56.5, 67.5]:
    for i in range(2):
        for j in range(2):
            box(ax, x0 + 4 * i, 44 + 4 * j, 4, 4, 'sujet', r=0.3, lw=0.5)
    box(ax, x0 - 0.6, 43.4, 9.2, 9.2, 'varie', fill=False, dash=True, lw=0.8, r=0.3)
brace(ax, 12.5, 75.5, 41, 'resultat', label='24 / 4 = 6 groupes', size='m')
line(ax, [(6, 29), (82, 29)], 'fixe')
text(ax, 44, 22, r'$\binom{10}{3}=10!\,/\,(3!\times 7!)$', 'fixe', 'm')
text(ax, 38, 12, '3 628 800 / (6 × 5 040)', 'fixe', 'm')
text(ax, 63, 12, '= 120', 'resultat', 'm', weight='bold')
save(fig, '01-173')
