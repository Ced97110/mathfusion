import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
gx, gy, c = 4, 22, 9
for r_ in range(4):
    for c_ in range(4):
        x, y = gx + c_ * c, gy + (3 - r_) * c
        if r_ == c_: box(ax, x, y, c - 1, c - 1, 'fixe', fill=False, dash=True)
        elif c_ > r_: box(ax, x, y, c - 1, c - 1, 'resultat')
        else: box(ax, x, y, c - 1, c - 1, 'fixe')
text(ax, 21, 62, 'groupe de 4 personnes', 'encre', 's')
text(ax, 21, 17, '4 × 3 = 12 couples', 'encre', 's')
text(ax, 21, 11, '12 ÷ 2 = 6 paires', 'resultat', 's')
box(ax, 46, 50, 6, 6, 'resultat'); text(ax, 54, 53, 'paire retenue', 'encre', 's', ha='left')
box(ax, 46, 40, 6, 6, 'fixe'); text(ax, 54, 43, 'déjà comptée', 'encre', 's', ha='left')
box(ax, 46, 30, 6, 6, 'fixe', fill=False, dash=True); text(ax, 54, 33, 'même personne', 'encre', 's', ha='left')
text(ax, 66, 21, r'$n \times (n - 1) \div 2$', 'sujet', 'l')
text(ax, 44, 4, '1000 × 999 ÷ 2 = 499 500', 'sujet', 'm')
save(fig, '53-004')
