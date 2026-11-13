import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
k, ox1, oy1, ox2, oy2 = 0.32, 10, 60, 10, 14
fig, ax = canvas(100)
# L-shape : carré de côté 110 privé du carré de côté 40 (coin haut droit)
poly(ax, [(ox1, oy1), (ox1 + 110*k, oy1), (ox1 + 110*k, oy1 + 70*k), (ox1, oy1 + 70*k)], 'sujet')
poly(ax, [(ox1, oy1 + 70*k), (ox1 + 70*k, oy1 + 70*k), (ox1 + 70*k, oy1 + 110*k), (ox1, oy1 + 110*k)], 'varie')
box(ax, ox1 + 70*k, oy1 + 70*k, 40*k, 40*k, 'fixe', fill=False, dash=True, label='a = 40', size='s', r=0.3)
brace(ax, ox1, ox1 + 110*k, oy1, 'sujet', label='b + c = 110', down=True)
text(ax, 55, oy1 + 14, '110² − 40² = 10 500', 'sujet', 'm', ha='left')
# déplacement du morceau orange
arrow(ax, (ox1 + 17, oy1 - 8), (ox1 + 17, oy2 + 70*k*0 + 28*0.32/0.32 + 8), 'varie')
text(ax, ox1 + 20, 47.5, 'on déplace le morceau orange', 'varie', 's', ha='left')
# rectangle 150 × 70
poly(ax, [(ox2, oy2), (ox2 + 110*k, oy2), (ox2 + 110*k, oy2 + 70*k), (ox2, oy2 + 70*k)], 'sujet')
poly(ax, [(ox2 + 110*k, oy2), (ox2 + 150*k, oy2), (ox2 + 150*k, oy2 + 70*k), (ox2 + 110*k, oy2 + 70*k)], 'varie')
brace(ax, ox2, ox2 + 150*k, oy2, 'sujet', label='150 = 110 + 40', down=True)
text(ax, 61, 30, '70 = 110 − 40', 'sujet', 'm', ha='left')
text(ax, 61, 23, '150 × 70 = 10 500', 'resultat', 'm', ha='left')
text(ax, 61, 16, '÷ 6 000 = 1,75', 'resultat', 'm', ha='left')
save(fig, '37-084')
