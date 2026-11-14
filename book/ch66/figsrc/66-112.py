import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
poly(ax, [(14, 62), (44, 62), (44, 70), (14, 70)], 'sujet')
poly(ax, [(44, 62), (74, 62), (74, 70), (44, 70)], 'fixe')
text(ax, 29, 66, '1/2', 'sujet', 'm')
brace(ax, 14, 74, 71, 'fixe', label='longueur 1', down=False)
text(ax, 62, 55, '1 ÷ 2', 'varie', 'm')
B = [(2, 2, 84, 44, 'fixe', 'réels ℝ'), (5, 5, 78, 34, 'varie', 'algébriques'),
     (8, 8, 72, 24, 'resultat', 'constructibles'), (11, 11, 66, 14, 'sujet', 'rationnels ℚ')]
for x, y, w, h, r, nom in B:
    box(ax, x, y, w, h, r, r=1.2)
    text(ax, x + 3, y + h - 3.5, nom, r, 's', ha='left', weight='bold')
arrow(ax, (44, 61.5), (44, 17.5), 'varie')
disc(ax, 44, 16, 1.4, 'sujet')
text(ax, 52, 16, '1/2', 'sujet', 'm', ha='left')
save(fig, '66-112')
