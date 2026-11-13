import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
specs = [(2, r"paquet $1K$", [('1', 'sujet'), ('5', 'varie')]), (32, r"paquet $2K$", [('2', 'sujet'), ('10', 'varie')]),
         (62, r"paquet $3K$", [('3', 'sujet'), ('15', 'varie')])]
for x, lab, els in specs:
    box(ax, x, 22, 24, 20, 'fixe')
    text(ax, x + 12, 37, lab, 'fixe', 's')
    for i, (v, r) in enumerate(els):
        disc(ax, x + 7 + 10 * i, 28, 4, r, label=v, size='s')
text(ax, 28.5, 32, "+", 'encre', 'l'); text(ax, 58.5, 32, "=", 'encre', 'l')
text(ax, 22, 14, r"$1+2=3$", 'sujet', 'm'); text(ax, 66, 14, r"$5+10=15$", 'varie', 'm')
text(ax, 44, 4, "K normal : même paquet", 'resultat', 's')
save(fig, '48-075')
