import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
q, x0 = 12, 20
for k in range(4):
    box(ax, x0 + k * q, 54, q, 8, 'varie')
brace(ax, x0, x0 + 4 * q, 54, 'sujet', label='1 litre = 4 verres')
for k in range(4):
    box(ax, x0 + k * q, 32, q, 8, 'varie' if k < 3 else 'fixe', dash=(k == 3), fill=(k < 3))
brace(ax, x0, x0 + 3 * q, 32, 'sujet', label=r'$\frac{3}{4}$ de litre = 3 verres')
box(ax, 6, 3, 36, 10, 'resultat', label=r'$\frac{3}{4}\div\frac{1}{4}=3$')
box(ax, 46, 3, 36, 10, 'resultat', label=r'$\frac{3}{4}\times4=3$')
text(ax, 44, 8, '=', 'resultat', 'l')
save(fig, '06-060')
