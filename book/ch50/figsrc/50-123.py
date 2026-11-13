import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X0, BW, Y = 8, 16, 44
for i in range(3):
    box(ax, X0 + i * BW, Y, BW, 8, 'sujet' if i == 0 else 'fixe', label=None)
    for j in range(2):
        pass
text(ax, X0 + BW / 4, Y + 4, '$e$', 'sujet', 's'); text(ax, X0 + 3 * BW / 4, Y + 4, r'$s_A$', 'sujet', 's')
brace(ax, X0, X0 + 3 * BW, Y + 8, 'sujet', label=r'$|G|=6$', down=False)
text(ax, 72, Y + 4, 'indice 3 :\n2 ne le divise pas', 'fixe', 's')
arrow(ax, (X0 + BW / 2, Y), (X0 + BW / 2, 25), 'varie')
box(ax, 6, 6, 44, 19, 'sujet', label='$p^k=2$ divise $|C(y)|=2$\ngroupe plus petit :\nrécurrence ici', size='s')
save(fig, '50-123')
