import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 20, 66, 48, 9, 'sujet', label=r'racine commune $y_0=2$')
for xc, lab, val in [(18, r'$y_0^2$', '4'), (44, r'$y_0$', '2'), (70, '1', '1')]:
    arrow(ax, (44, 66), (xc, 57), 'fixe')
    text(ax, xc, 54, lab, 'fixe', 'm')
    box(ax, xc - 9, 40, 18, 9, 'resultat', label=val, size='l')
text(ax, 44, 33, r'$(4,\ 2,\ 1)\neq(0,\ 0,\ 0)$', 'resultat', 's')
for y, s in [(24, r'ligne de $f$ : $4-10+6=0$'), (16, r'ligne de $yg$ : $4-4=0$'), (8, r'ligne de $g$ : $2-2=0$')]:
    text(ax, 44, y, s, 'resultat', 's')
save(fig, '70-031')
