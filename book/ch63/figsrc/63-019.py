import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 4, 84, 54, 'sujet')
text(ax, 44, 52, r'$G=\{1,\sigma,\tau,\sigma\tau\}$', 'sujet', 'l')
cells = [(6, 28, '1 : ne change rien', 'fixe'), (48, 28, r'$\sigma$ : change $\sqrt{2}$', 'varie'),
         (6, 8, r'$\tau$ : change $\sqrt{3}$', 'varie'), (48, 8, r'$\sigma\tau$ : change les deux', 'varie')]
for x, y, lab, role in cells:
    box(ax, x, y, 36, 16, role, label=lab, size='m')
save(fig, '63-019')
