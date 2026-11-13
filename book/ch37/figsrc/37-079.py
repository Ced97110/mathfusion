import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
x0, u = 10, 0.9
fig, ax = canvas(60)
box(ax, x0, 38, 40*u, 8, 'varie', label='40 = a', r=0.6)
box(ax, x0 + 40*u, 38, 35*u, 8, 'resultat', label='35 = s − a', r=0.6)
brace(ax, x0, x0 + 75*u, 46, 'sujet', label='s = 75', down=False)
box(ax, x0, 14, 35*u, 8, 'resultat', label='35', r=0.6)
box(ax, x0 + 35*u, 14, 35*u, 8, 'resultat', label='35', r=0.6)
brace(ax, x0, x0 + 70*u, 14, 'sujet', label='b + c − a = 70', down=True)
text(ax, 44, 29, 'les deux lectures : 35', 'resultat', 'm')
save(fig, '37-079')
