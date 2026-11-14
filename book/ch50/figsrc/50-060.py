import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X0, CW, CH = 14.0, 10.0, 8.0
for i in range(6):
    role = 'sujet' if i < 2 else 'fixe'
    lab = ['$e$', '$s_A$'][i] if i < 2 else None
    box(ax, X0 + i * CW, 54, CW - 0.8, CH, role, label=lab, size='s', r=0.5)
brace(ax, X0, X0 + 2 * CW - 0.8, 53, 'sujet', label=r'$N(H)$ : 2 éléments', down=True, size='s')
brace(ax, X0 + 2 * CW, X0 + 6 * CW - 0.8, 53, 'fixe', label='4 autres éléments', down=True, size='s')
text(ax, 44, 34, 'sous-groupes de 2 éléments', 'encre', 's')
labs = [r'$\{e, s_A\}$', r'$\{e, s_B\}$', r'$\{e, s_C\}$']
for k, lab in enumerate(labs):
    box(ax, 4.5 + k * 27.5, 20, 26, 9, 'sujet' if k == 0 else 'autre', label=lab, size='s')
text(ax, 44, 7, r'$[G : N(H)] = 6\,/\,2 = 3$', 'resultat', 'm')
save(fig, '50-060')
