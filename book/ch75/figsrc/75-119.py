import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 11
text(ax, 44, 60, '4 coordonnées, 2 choix chacune', 'encre', 's')
for i in range(16):
    c, r = i % 4, i // 4
    x, y = 4 + c * (s + 2), 8 + (3 - r) * (s + 2)
    box(ax, x, y, s, s, 'limite' if i == 0 else 'resultat', label='0' if i == 0 else None, size='m')
text(ax, 68, 40, '16 vecteurs', 'encre', 's', ha='left')
text(ax, 62, 48, '', 'encre', 's')
text(ax, 66, 24, '0 : exclu', 'limite', 's', ha='left')
text(ax, 66, 14, '15 choix de e', 'resultat', 's', ha='left')
save(fig, '75-119')
