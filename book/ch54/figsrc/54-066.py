import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, 'anneau $D$', 'sujet', 'm')
text(ax, 66, 59, r'corps $F_D$', 'resultat', 'm')
left = [('ℤ', 46), ('ℤ[x]', 32), ('ℚ[x]', 18)]
for lab, y in left:
    box(ax, 11, y - 4.5, 22, 9, 'sujet', label=lab)
box(ax, 55, 41.5, 22, 9, 'resultat', label='ℚ')
box(ax, 55, 20.5, 22, 9, 'resultat', label='ℚ(x)')
arrow(ax, (34, 46), (54, 46), 'resultat')
arrow(ax, (34, 32), (54, 26), 'resultat')
arrow(ax, (34, 18), (54, 24), 'resultat')
text(ax, 44, 7, 'deux anneaux, un même corps', 'resultat', 's')
save(fig, '54-066')
