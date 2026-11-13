import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(106)
mats = ['(2, 4)   (4, 2)   (6, 6)', '(2, 4)   (4, 2)   (0, 0)', '(2, 0)   (4, −6)   (0, 0)',
        '(2, 0)   (0, −6)   (0, 0)', '(2, 0)   (0, 6)   (0, 0)']
ops = [r'$L_3\leftarrow L_3-L_1-L_2$', r'$C_2\leftarrow C_2-2C_1$', r'$L_2\leftarrow L_2-2L_1$', r'$L_2\leftarrow -L_2$']
text(ax, 27, 101, 'lignes du tableau', 'fixe', 's')
ys = [84, 66, 48, 30, 12]
for i, (m, y) in enumerate(zip(mats, ys)):
    last = i == len(mats) - 1
    box(ax, 2, y, 50, 11, 'resultat' if last else 'sujet', label=m, size='s')
    if not last:
        arrow(ax, (27, y), (27, ys[i + 1] + 11.5), 'varie')
        text(ax, 56, y - 3.5, ops[i], 'varie', 's', ha='left')
text(ax, 56, 17.5, r'$=\mathrm{diag}(2,\,6)$', 'resultat', 's', ha='left')
text(ax, 56, 7, '+ une ligne nulle', 'fixe', 's', ha='left')
save(fig, '59-137')
