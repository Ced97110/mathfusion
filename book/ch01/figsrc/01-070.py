import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
xs = [6.5, 19.5, 29.5, 39.5, 52.5, 62.5, 72.5]
roles = ['sujet', 'autre'] + ['fixe'] * 5
for x, d, r in zip(xs, '2500000', roles):
    box(ax, x, 20, 9, 10, r, label=d, size='l', lw=1.4 if r == 'sujet' else 0.8)
brace(ax, 6.5, 15.5, 32, 'sujet', down=False)
text(ax, 3, 35.7, 'nouveau groupe', 'sujet', 's', ha='left')
brace(ax, 19.5, 48.5, 32, 'fixe', down=False)
brace(ax, 52.5, 81.5, 32, 'fixe', down=False)
arrow(ax, (81.5, 40), (13, 40), 'fixe', lw=0.7)
text(ax, 50, 43, '7e case depuis la droite'.replace('7e', r'7$^{\mathrm{e}}$'), 'fixe', 's')
text(ax, 3, 49, 'millions = 1 000 × 1 000', 'sujet', 's', ha='left')
arrow(ax, (11, 20), (11, 14.5), 'resultat')
arrow(ax, (24, 20), (24, 8.5), 'resultat')
text(ax, 11, 12, '2 000 000', 'resultat', 'm')
text(ax, 24, 6, '500 000', 'resultat', 'm')
save(fig, '01-070')
