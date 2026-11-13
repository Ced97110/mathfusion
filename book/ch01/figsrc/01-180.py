import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for x, lab in zip([26, 38, 50, 62], ['1', '3', '3', '1']):
    role = 'sujet' if lab == '3' else 'fixe'
    disc(ax, x, 40, 4, role, label=lab, size='l', lw=1.2 if role == 'sujet' else 0.8)
text(ax, 38, 48, '(3 1)', 'sujet', 'm')
text(ax, 50, 48, '(3 2)', 'sujet', 'm')
for x, lab in zip([20, 32, 44, 56, 68], ['1', '4', '6', '4', '1']):
    role = 'resultat' if lab == '6' else 'fixe'
    disc(ax, x, 24, 4, role, label=lab, size='l', lw=1.2 if role == 'resultat' else 0.8)
text(ax, 44, 15, '(4 2)', 'resultat', 'm')
arrow(ax, (38, 36), (42.5, 28), 'varie', lw=1.1)
arrow(ax, (50, 36), (45.5, 28), 'varie', lw=1.1)
text(ax, 44, 6, '(3 1) + (3 2) = 3 + 3 = 6', 'encre', 'm')
save(fig, '01-180')
