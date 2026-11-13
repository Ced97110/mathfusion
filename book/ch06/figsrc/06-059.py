import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
q, x0 = 18, 17
text(ax, 44, 61, r'$\frac{3}{4}\div\frac{1}{4}=3$', 'resultat', 'xl')
for k in range(3):
    box(ax, x0 + k * q, 38, q, 8, 'sujet')
brace(ax, x0, x0 + 3 * q, 46, 'sujet', label=r'$\frac{3}{4}$ de litre', down=False)
for k in range(3):
    arrow(ax, (x0 + k * q + q / 2, 38), (x0 + k * q + q / 2, 24), 'varie')
    box(ax, x0 + k * q + 2, 14, q - 4, 9, 'varie', label=r'$\frac{1}{4}$')
text(ax, 44, 5, '3 verres, sans reste', 'resultat', 'm')
save(fig, '06-059')
