import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'carré : $\alpha^{k}\to\alpha^{2k}$ (mod 15)', 'encre', 'm')
for y, a, b, lab, curve, ya in [(52, 5, 10, '5 × 2 = 10', -0.5, 55), (22, 9, 3, '9 × 2 = 18, 18 − 15 = 3', 0.4, 25)]:
    f = numberline(ax, 6, 76, y, 0, 14, 1, labels=False, arrow_right=False)
    disc(ax, f(a), y, 2.2, 'sujet')
    disc(ax, f(b), y, 2.2, 'resultat')
    arrow(ax, (f(a), ya), (f(b), ya), 'varie', curve=curve)
    text(ax, (f(a) + f(b)) / 2, ya + abs(curve) * abs(f(b) - f(a)) / 2 + 3.2, lab, 'varie', 'm')
    text(ax, f(a), y - 8, rf'$\alpha^{{{a}}}$', 'sujet', 'm')
    text(ax, f(b), y - 8, rf'$\alpha^{{{b}}}$', 'resultat', 'm')
text(ax, 44, 5, 'un trait = un exposant de 0 à 14', 'fixe', 's')
save(fig, '67-182')
