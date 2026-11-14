import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
steps = [(84, 'fixe', r'$p=0,\ q=-2,\ d=-108$'),
         (68, 'fixe', r'$-3d=324,\ \sqrt{324}=18$'),
         (52, 'varie', r'$z_1^3=54,\ z_2^3=0$'),
         (36, 'varie', r'$z_1=3\sqrt[3]{2},\ z_2=0$')]
for y, role, lab in steps:
    box(ax, 4, y, 54, 10, role, label=lab, size='s')
for y in (84, 68, 52):
    arrow(ax, (31, y), (31, y - 6), 'varie')
text(ax, 60, 41, r'$z_1z_2=0=-3p$', 'resultat', 's', ha='left')
roots = [r'$y_1=\sqrt[3]{2}$', r'$y_2=w^2\sqrt[3]{2}$', r'$y_3=w\sqrt[3]{2}$']
for k, r in enumerate(roots):
    box(ax, 3 + k * 29, 6, 27, 12, 'resultat', label=r, size='s')
for x0, x1 in ((18, 16.5), (31, 44.5), (44, 72.5)):
    arrow(ax, (x0, 36), (x1, 18.5), 'resultat')
save(fig, '65-124')
