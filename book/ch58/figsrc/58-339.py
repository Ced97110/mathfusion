import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# les 8 listes de 3 bits ; le code en garde 4, stables par somme ; la base en a 2
w, h, g = 17.0, 10.0, 2.0
x0 = (88 - (4 * w + 3 * g)) / 2
code = [('000', 'sujet'), ('110', 'varie'), ('011', 'autre'), ('101', 'sujet')]
hors = ['001', '010', '100', '111']
text(ax, 44, 74, 'Listes de 3 bits : 8 au total', 'fixe', 'm')
for k, v in enumerate(hors):
    box(ax, x0 + k * (w + g), 58, w, h, 'fixe', fill=False, label=v, size='m', dash=True)
text(ax, 44, 48, 'Le code garde 4 listes', 'sujet', 'm', weight='bold')
for k, (v, role) in enumerate(code):
    box(ax, x0 + k * (w + g), 32, w, h, role, label=v, size='m', weight='bold' if role != 'sujet' else 'normal')
# la somme de deux listes du code reste dans le code : 110 + 011 = 101
xa, xb, xc = (x0 + 1 * (w + g) + w / 2, x0 + 2 * (w + g) + w / 2, x0 + 3 * (w + g) + w / 2)
arrow(ax, (xa, 31), (xc - 3, 31), 'resultat', lw=1.0, curve=0.35)
arrow(ax, (xb, 31), (xc, 31), 'resultat', lw=1.0, curve=0.35)
text(ax, 44, 16, r'$110 + 011 = 101$ : encore dans le code', 'resultat', 's')
text(ax, 44, 7, 'base : 110 et 011, dimension 2', 'resultat', 'm', weight='bold')
save(fig, '58-339')
