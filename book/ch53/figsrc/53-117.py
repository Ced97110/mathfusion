import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
steps = ['27 − 16 = 11', '11 − 8 = 3', '3 − 2 = 1', '1 − 1 = 0']
for i, s in enumerate(steps):
    y = 56 - i * 14
    box(ax, 4, y, 34, 9, 'resultat' if i == 3 else 'varie', label=s, size='m')
    if i < 3: arrow(ax, (21, y - 0.5), (21, y - 4.5), 'varie')
text(ax, 21, 5, 'reste 0 : on s’arrête', 'resultat', 's')
text(ax, 62, 64, 'retirés : 16, 8, 2, 1', 'sujet', 's')
text(ax, 62, 48, '4 : pas retiré, donc 0', 'fixe', 's')
box(ax, 46, 22, 32, 12, 'sujet', label='11011', size='l')
text(ax, 62, 16, 'les cinq bits', 'sujet', 's')
save(fig, '53-117')
