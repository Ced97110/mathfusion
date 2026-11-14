import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
r1 = -2.9859
text(ax, 26, 72, r'$r_1$ approché à volonté', 'resultat', 'm', weight='bold')
text(ax, 71, 72, 'écrire', 'limite', 'm', weight='bold')
for y, (a, b, lab) in zip((58, 44, 30), ((-3, -2.9, '0,1'), (-2.99, -2.98, '0,01'), (-2.986, -2.985, '0,001'))):
    assert a <= r1 <= b
    line(ax, [(14, y), (50, y)], 'sujet', lw=1.0)
    for x in (14, 50): line(ax, [(x, y - 1.5), (x, y + 1.5)], 'sujet', lw=0.8)
    disc(ax, 14 + 36 * (r1 - a) / (b - a), y, 1.4, 'resultat')
    text(ax, 2, y, lab, 'sujet', 's', ha='left')
text(ax, 26, 20, 'longueur de l’intervalle', 'fixe', 's')
text(ax, 26, 8, r'$r_1\approx-2{,}9859$', 'resultat', 'm')
box(ax, 56, 36, 30, 16, 'limite', label='expression finie\nen radicaux', size='s')
text(ax, 71, 28, 'n’existe pas', 'limite', 'm')
save(fig, '64-184')
