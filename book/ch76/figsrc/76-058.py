import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'partie de $\{1,2,3\}$ : monôme', 'fixe', 's')
labs = [r'$\emptyset$' + '\n1', r'$\{1\}$' + '\n' + r'$e_1$', r'$\{2\}$' + '\n' + r'$e_2$', r'$\{3\}$' + '\n' + r'$e_3$',
        r'$\{1,2\}$' + '\n' + r'$e_1\wedge e_2$', r'$\{1,3\}$' + '\n' + r'$e_1\wedge e_3$',
        r'$\{2,3\}$' + '\n' + r'$e_2\wedge e_3$', r'$\{1,2,3\}$' + '\n' + r'$e_1\wedge e_2\wedge e_3$']
for k, lab in enumerate(labs):
    r, c = divmod(k, 4)
    box(ax, 1.5 + c * 21.6, 30 - r * 20 + 6, 20.5, 16, 'sujet', label=lab, size='s')
box(ax, 14, 2, 60, 10, 'resultat', label=r'8 parties = 8 monômes = $2^3$')
save(fig, '76-058')
