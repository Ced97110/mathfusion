import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$b_2 = a_1a_3 - 4a_4$', 'sujet', 'l')
s = 0.12
x0 = 14.0
w_rest, w_out = 404 * s, 96 * s
box(ax, x0, 38, w_rest, 8, 'resultat', r=0.6)
box(ax, x0 + w_rest, 38, w_out, 8, 'varie', r=0.6)
brace(ax, x0, x0 + 500 * s, 47, 'sujet', r'$a_1a_3 = 10 \times 50 = 500$', down=False)
brace(ax, x0, x0 + w_rest, 37, 'resultat', 'reste', down=True)
brace(ax, x0 + w_rest + 0.5, x0 + 500 * s, 37, 'varie', r'$4a_4 = 96$', down=True)
arrow(ax, (44, 26), (44, 21), 'fixe')
box(ax, 14, 8, 60, 12, 'resultat', label=r'$b_2 = 500 - 96 = 404$', size='m')
text(ax, 44, 2.5, r'= $14\times 11 + 14\times 10 + 11\times 10$', 'fixe', 's')
save(fig, '65-089')
