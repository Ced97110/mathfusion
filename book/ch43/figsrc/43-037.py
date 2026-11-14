import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
Y = lambda v: 14 + (v + 7) * 2.4
X0, RUN, RISE = 20, 14, 17
arrow(ax, (X0, Y(-7) - 4), (X0, Y(5) + 6), 'fixe', lw=0.8)
text(ax, X0, Y(5) + 9.5, 'hauteur à 0', 'fixe', 's')
for v, n, r in [(5, 'f', 'sujet'), (1, 'g', 'autre'), (-7, 'h', 'fixe')]:
    line(ax, [(X0, Y(v)), (X0 + RUN, Y(v) + RISE)], r, lw=1.2)
    disc(ax, X0, Y(v), 1.0, r)
    text(ax, X0 - 2, Y(v), f'{v}'.replace('-', '−'), r, 's', ha='right')
    text(ax, X0 + RUN + 2.5, Y(v) + RISE + 1.5, n, r, 's')
xe = X0 + RUN + 5
for a, b, lab in [(5, 1, '4'), (1, -7, '8')]:
    arrow(ax, (xe, Y(a) + RISE), (xe, Y(b) + RISE), 'varie', both=True); text(ax, xe + 1.8, (Y(a) + Y(b)) / 2 + RISE, lab, 'varie', 'm', ha='left')
arrow(ax, (xe + 9, Y(5) + RISE), (xe + 9, Y(-7) + RISE), 'resultat', both=True)
text(ax, xe + 10.8, (Y(5) + Y(-7)) / 2 + RISE, '12', 'resultat', 'm', ha='left')
text(ax, 70, 64, r'$f-g$ fixe : trois conditions', 'sujet', 's')
text(ax, 30, 4, 'trois droites de pente 2', 'fixe', 's')
box(ax, 56, 46, 30, 10, 'fixe', label=r'$f-f=0$', size='s')
box(ax, 56, 32, 30, 10, 'fixe', label=r'$g-f=-c$', size='s')
box(ax, 56, 10, 30, 18, 'resultat')
text(ax, 71, 23, r'$(f-g)+(g-h)$', 'resultat', 's'); text(ax, 71, 15, r'$4+8=12$', 'resultat', 'm')
save(fig, '43-037')
