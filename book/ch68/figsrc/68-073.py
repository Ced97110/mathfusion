import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
y = 28
f = numberline(ax, 8, 68, y, 0, 3, 1, arrow_right=True)
cases = [(0.5, 0, r'$\lfloor 0{,}5\rfloor=0$'), (1.5, 1, r'$\lfloor 1{,}5\rfloor=1$'), (2, 2, r'$\lfloor 2\rfloor=2$')]
for a, fl, lab in cases:
    if a != fl:
        disc(ax, f(a), y, 1.7, 'varie')
        arrow(ax, (f(a) - 2, y + 2.2), (f(fl) + 2, y + 2.2), 'varie', curve=0.6)
    disc(ax, f(fl), y, 1.7, 'resultat')
    text(ax, (f(a) + f(fl)) / 2, 42, lab, 'encre', 's')
disc(ax, 6, 8, 1.7, 'varie'); text(ax, 10, 8, 'le nombre $a$', 'varie', 's', ha='left')
disc(ax, 44, 8, 1.7, 'resultat'); text(ax, 48, 8, r'son arrondi vers le bas', 'resultat', 's', ha='left')
save(fig, '68-073')
