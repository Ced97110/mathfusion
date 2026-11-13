import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
q, x0 = 20, 14
rows = [(52, '12 ÷ 4 : combien de fois 4 ?', '12', '4'), (12, r'$\frac{3}{4}$ ÷ $\frac{1}{4}$ : combien de $\frac{1}{4}$ ?', r'$\frac{3}{4}$', r'$\frac{1}{4}$')]
for y, title, tot, part in rows:
    for k in range(3):
        box(ax, x0 + k * q, y, q, 8, 'varie', label=part)
    brace(ax, x0, x0 + 3 * q, y + 8, 'sujet', label=tot, down=False)
    brace(ax, x0, x0 + 3 * q, y, 'resultat', label='3 fois')
    text(ax, x0 + 1.5 * q, y + 20, title, 'encre', 'm')
save(fig, '06-058')
