import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(102)
cw, g, xe = 8, 1.5, 84
def row(y, digits, roles):
    n = len(digits)
    for i, (d, r) in enumerate(zip(digits, roles)):
        x = xe - (n - i) * (cw + g) + g
        box(ax, x, y - 5, cw, 10, r if d == '0' else 'fixe', label=d, size='l')
row(92, '10', ['sujet'] * 2); row(74, '100', ['autre'] * 3)
row(52, '1000', ['sujet', 'sujet', 'autre', 'autre'])
text(ax, 4, 92, r'$10^1$ : 1 zéro', 'sujet', 'm', ha='left')
text(ax, 4, 74, r'$10^2$ : 2 zéros', 'autre', 'm', ha='left')
text(ax, 4, 52, r'$10^3$ : 3 zéros', 'resultat', 'm', ha='left')
text(ax, 40, 83, r'$\times$', 'encre', 'xl'); text(ax, 40, 63, '=', 'encre', 'xl')
text(ax, 44, 40, '1 + 2 = 3 zéros', 'varie', 'm', weight='bold')
line(ax, [(4, 32), (84, 32)], 'fixe', dash=True)
text(ax, 44, 25, 'même règle pour les décimales', 'fixe', 's')
text(ax, 44, 15, r'$0{,}1\times0{,}01=0{,}001$', 'sujet', 'l')
text(ax, 44, 6, '1 + 2 = 3 décimales', 'varie', 'm', weight='bold')
save(fig, '08-052')
