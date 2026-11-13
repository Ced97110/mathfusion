import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
cells = [('les deux fractions', 'fixe', r'$\frac{3}{4}$ et $\frac{1}{2}$'),
         ('somme', 'sujet', r'$\frac{3}{4} + \frac{1}{2} = \frac{5}{4}$'),
         ('différence', 'sujet', r'$\frac{3}{4} - \frac{1}{2} = \frac{1}{4}$'),
         ('produit', 'sujet', r'$\frac{3}{4} \times \frac{1}{2} = \frac{3}{8}$'),
         ('quotient', 'sujet', r'$\frac{3}{4} \div \frac{1}{2} = \frac{3}{2}$'),
         ('comparaison', 'autre', r'$\frac{3}{4} > \frac{1}{2}$')]
for k, (lab, role, expr) in enumerate(cells):
    x = 2 + (k % 2) * 44; y = 56 - (k // 2) * 26
    box(ax, x, y, 40, 22, role)
    text(ax, x + 20, y + 17, lab, role, 's', weight='bold')
    text(ax, x + 20, y + 8.5, expr, role, 'm')
save(fig, '07-074')
