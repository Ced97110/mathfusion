import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
labs = [r'$\lambda^4$', r'$-4\lambda^3$', r'$-4\lambda^2$', r'$+16\lambda$', r'$-8$']
roles = ['fixe', 'resultat', 'varie', 'varie', 'resultat']
for i, (s, r) in enumerate(zip(labs, roles)):
    box(ax, 2 + i * 17, 36, 16, 12, r, label=s, size='s')
text(ax, 27, 31, 'trace', 'resultat', 's'); text(ax, 78, 31, 'norme', 'resultat', 's')
brace(ax, 37, 70, 54, 'varie', label='transmis ?', down=False)
text(ax, 44, 16, 'produits 2 à 2 : somme −4', 'varie', 's')
text(ax, 44, 8, 'produits 3 à 3 : somme −16', 'varie', 's')
save(fig, '77-149')
