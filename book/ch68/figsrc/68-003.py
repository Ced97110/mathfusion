import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
p = [0.999, 0.999 ** 2, 0.999 ** 10000]
labs = [r'1 bit : $0{,}999$',
        r'2 bits : $0{,}999\times0{,}999\approx0{,}998$',
        r'10 000 bits : $0{,}999^{10\,000}\approx0{,}00005$']
L = 76
for k, (y, v, s) in enumerate(zip([44, 30, 16], p, labs)):
    text(ax, 4, y + 8, s, 'encre', 'm', ha='left')
    if k < 2:
        poly(ax, [(4, y), (4 + L * v, y), (4 + L * v, y + 5), (4, y + 5)], 'resultat')
    else:
        line(ax, [(4, y - 0.5), (4, y + 5.5)], 'resultat', lw=1.6)
        text(ax, 8, y + 2.5, 'à peine un trait', 'resultat', 's', ha='left')
numberline(ax, 4, 80, 8, 0, 1, step=1, arrow_right=False)
text(ax, 42, 3, 'probabilité d’arriver intacte', 'fixe', 's')
save(fig, '68-003')
