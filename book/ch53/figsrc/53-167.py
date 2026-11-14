import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X0, X1 = 8, 76
text(ax, X0, 58, 'chiffres décimaux', 'sujet', 's', ha='left', weight='bold')
f = numberline(ax, X0, X1, 48, 0, 600, step=200, arrow_right=False, role='sujet', tick=1.4)
disc(ax, f(600), 48, 1.4, 'sujet')
# règle des bits
text(ax, X0, 28, 'bits', 'autre', 's', ha='left', weight='bold')
g = numberline(ax, X0, X1, 18, 0, 2048, step=512, labels=False, arrow_right=False, role='autre', tick=1.4)
for v in (0, 512, 1024, 1536, 2048):
    text(ax, g(v), 18 - 4, f'{v:,}'.replace(',', ' '), 'autre', 's')
disc(ax, g(2048), 18, 1.4, 'autre')
line(ax, [(X1, 40), (X1, 20)], 'resultat', lw=1.0, dash=True)
text(ax, X1 - 1.5, 30, 'même clé', 'resultat', 's', ha='right')
text(ax, 44, 4, 'plus de 3 bits par chiffre', 'fixe', 's')
save(fig, '53-167')
