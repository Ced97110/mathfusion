import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 45, 46, r'Nombres : $x = 3$', 'limite', 'm'); text(ax, 73, 46, r'Parties : $A$', 'resultat', 'm')
for y, lab, a, b in ((26, r'$x + x = 0$ ?', r'$3 + 3 = 6 \neq 0$', r'$A + A = \varnothing$'),
                     (8, r'$x^2 = x$ ?', r'$3 \times 3 = 9 \neq 3$', r'$A \times A = A$')):
    text(ax, 2, y + 6, lab, 'encre', 'm', ha='left')
    box(ax, 33, y, 26, 12, 'limite', label=a, size='s'); box(ax, 60, y, 26, 12, 'resultat', label=b, size='s')
save(fig, '80-317')
