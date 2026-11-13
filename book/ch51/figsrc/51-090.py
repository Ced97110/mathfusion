import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
c = 7.5
def mat(x0, y0, roles, vals):
    for i in range(2):
        for j in range(2):
            box(ax, x0 + j * c, y0 + (1 - i) * c, c, c, roles[2 * i + j], label=vals[2 * i + j], size='m')
mat(4, 32, ['sujet', 'sujet', 'varie', 'varie'], ['1', '2', '0', '3'])
mat(36, 32, ['varie', 'sujet', 'varie', 'sujet'], ['4', '5', '0', '6'])
mat(68, 32, ['sujet', 'sujet', 'resultat', 'sujet'], ['4', '17', '0', '18'])
line(ax, [(22, 40), (28, 46)], 'encre'); line(ax, [(22, 46), (28, 40)], 'encre')
line(ax, [(54, 41), (60, 41)], 'encre'); line(ax, [(54, 45), (60, 45)], 'encre')
text(ax, 44, 52, 'ligne du bas × colonne de gauche', 'varie', 's')
text(ax, 44, 20, r'$0\times 4 + 3\times 0 = 0$', 'resultat', 'm')
text(ax, 44, 9, 'chaque terme a un facteur nul', 'resultat', 's')
save(fig, '51-090')
