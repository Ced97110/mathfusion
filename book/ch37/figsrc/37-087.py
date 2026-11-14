import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
u, x0 = 70 / 400, 9
fig, ax = canvas(56)
text(ax, 44, 51, 'côtés 3, 4, 5 : s = 6', 'fixe', 'm')
text(ax, 44, 43, '4 × 6 × 3 × 2 × 1 = 144', 'sujet', 'm')
arrow(ax, (x0 + 144*u/2, 39), (x0 + 144*u/2, 28), 'varie')
box(ax, x0, 16, 400*u, 10, 'fixe', fill=False, r=0.5)
box(ax, x0, 16, 144*u, 10, 'resultat', label='144', r=0.5)
brace(ax, x0, x0 + 400*u, 16, 'sujet', label='b² c² = 16 × 25 = 400', down=True)
text(ax, 44, 3, 'sin² A = 144 / 400 = 0,36', 'resultat', 'm', weight='bold')
save(fig, '37-087')
