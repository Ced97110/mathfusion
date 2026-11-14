import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# l'équivalence du théorème, barrée : elle est fausse ici
box(ax, 3, 72, 32, 10, 'sujet', label=r'$T(d)=0$')
box(ax, 53, 72, 32, 10, 'autre', label=r'$d=c-\eta(c)$')
text(ax, 44, 77, r'$\Leftrightarrow$', 'limite', 'xl')
line(ax, [(39, 73), (49, 81)], 'limite', lw=1.2)
# colonne de gauche : T(racine de 2) = 0
text(ax, 20, 63, r'conjugués de $\sqrt{2}$', 'sujet')
labs = [r'$\sqrt{2}$', r'$-\sqrt{2}$', r'$\sqrt{2}$', r'$-\sqrt{2}$']
for i, s in enumerate(labs):
    box(ax, 3 + i * 8.7, 50, 8, 9, 'sujet', label=s, size='s')
brace(ax, 3, 3 + 3 * 8.7 + 8, 50, 'resultat', label=r'somme $=0$')
box(ax, 3, 30, 35, 9, 'resultat', label=r'$T(\sqrt{2})=0$ vrai', size='s')
# colonne de droite : supposons racine de 2 = c - eta(c)
text(ax, 66, 63, 'supposons que', 'fixe')
box(ax, 47, 50, 38, 9, 'autre', label=r'$\sqrt{2}=c-\eta(c)$')
arrow(ax, (66, 50), (66, 44.8), 'fixe')
box(ax, 47, 36, 38, 9, 'autre', label=r'$\eta(\sqrt{2})=-\sqrt{2}$')
arrow(ax, (66, 36), (66, 30.8), 'fixe')
box(ax, 47, 22, 38, 9, 'limite', label=r'mais $\eta(\sqrt{2})=\sqrt{2}$')
save(fig, '67-152')
