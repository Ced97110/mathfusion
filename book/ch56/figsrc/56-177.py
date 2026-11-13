import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
assert round(3.2) == 3 and round(-0.6) == -1
text(ax, 44, 71, r'$q=3-i$', 'resultat', 'l', weight='bold')
def panel(y, lo, val, name, keep):
    f = numberline(ax, 10, 70, y, lo, lo + 1, 1, arrow_right=False)
    disc(ax, f(keep), y, 2.2, 'resultat')
    disc(ax, f(lo + (1 if keep == lo else 0)), y, 1.6, 'fixe')
    disc(ax, f(val), y, 1.6, 'varie')
    text(ax, f(val), y + 9, name, 'varie', 's')
    brace(ax, f(lo), f(val), y + 2.5, 'resultat' if keep == lo else 'fixe', label=f'{abs(val - lo):.1f}'.replace('.', ','), down=False)
    brace(ax, f(val), f(lo + 1), y + 2.5, 'fixe' if keep == lo else 'resultat', label=f'{abs(lo + 1 - val):.1f}'.replace('.', ','), down=False)
panel(50, 3, 3.2, r'$\mu=3{,}2$', 3)
panel(18, -1, -0.6, r'$\nu=-0{,}6$', -1)
text(ax, 76, 50, 'garde 3', 'resultat', 's', ha='left')
text(ax, 76, 18, r'garde $-1$', 'resultat', 's', ha='left')
save(fig, '56-177')
