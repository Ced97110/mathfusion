import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
steps = [(r'$u\in A$, $u\neq 0$', 'sujet'), (r'on suppose $e^u=w\in A$', 'autre'),
         (r'$w\cdot e^0-1\cdot e^u=0$', 'varie'), (r'coefficients de $A$, non nuls', 'varie'),
         ('contredit le théorème', 'limite'), (r'donc $e^u\notin A$', 'resultat')]
for i, (s, role) in enumerate(steps):
    y = 84 - i * 16.5
    box(ax, 14, y, 60, 10, role, label=s, size='s')
    if i < len(steps) - 1:
        arrow(ax, (44, y), (44, y - 6.3), 'fixe')
text(ax, 80, 71, '0 et $u$', 'fixe', 's', ha='center') if False else None
save(fig, '66-087')
