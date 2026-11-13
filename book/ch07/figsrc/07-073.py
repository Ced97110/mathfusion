import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
xl, xr = 20, 62
text(ax, xl, 84, 'entiers', 'fixe', 'm', weight='bold')
text(ax, xr, 84, 'fractions', 'sujet', 'm', weight='bold')
ys = [68, 48, 28]
L = [r'$2 + 3 \times 4$', r'$2 + 12$', r'$14$']
R = [r'$\frac{1}{2} + \frac{1}{3} \times \frac{1}{4}$', r'$\frac{1}{2} + \frac{1}{12}$',
     r'$\frac{6}{12} + \frac{1}{12} = \frac{7}{12}$']
for i, y in enumerate(ys):
    role = 'resultat' if i == 2 else 'fixe'
    text(ax, xl, y, L[i], role, 'm')
    text(ax, xr, y, R[i], 'resultat' if i == 2 else 'sujet', 'm')
for a, lab in [(0, '1. ×'), (1, '2. +')]:
    ym = (ys[a] + ys[a + 1]) / 2
    arrow(ax, (xl, ys[a] - 5), (xl, ys[a + 1] + 5), 'varie')
    arrow(ax, (xr, ys[a] - 7), (xr, ys[a + 1] + 7), 'varie')
    text(ax, 44, ym, lab, 'varie', 's')
line(ax, [(44, 78), (44, 22)], 'fixe', dash=True)
text(ax, 44, 8, 'dénominateur commun : pour +', 'varie', 's')
save(fig, '07-073')
