import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s = 18; x0, y0 = 18, 8
text(ax, x0 + s / 2 - 1, y0 + 3 * s - 4 + 2, '∘ = +', 'encre', 's') if False else None
lab = {0: 'pair = 0', 1: 'impair = 1'}; role = {0: 'sujet', 1: 'varie'}
for j in range(2):
    text(ax, 9, y0 + (1 - j) * s + s / 2 - 1, lab[j].replace(' = ', '\n= '), role[j], 's')
    text(ax, x0 + j * s + s / 2 - 1, y0 + 2 * s + 5, lab[j].replace(' = ', '\n= '), role[j], 's')
    for i in range(2):
        v = (i + j) % 2
        box(ax, x0 + i * s, y0 + (1 - j) * s, s - 2, s - 2, role[v], label=lab[v], size='s')
text(ax, 9, y0 + 2 * s + 5, '∘  ou  +', 'encre', 's')
text(ax, 44, 3.5, 'même table : S₃/A₃ ≅ ℤ/2ℤ', 'resultat', 's') if False else None
save(fig, '48-141')
