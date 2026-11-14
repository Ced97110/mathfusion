import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
els = [r'$\eta$', r'$\eta^2$', 'id']
for i, s in enumerate(els): box(ax, 8 + i * 25.5, 22, 22, 12, 'sujet', label=s, size='l')
brace(ax, 8, 82, 36, 'fixe', label=r'$Gal(E/F)$ : au plus $n=3$', down=False)
brace(ax, 8, 82, 20, 'sujet', label=r'$\langle\eta\rangle$ : 3 éléments', down=True)
text(ax, 44, 4, r'donc $Gal(E/F)=\langle\eta\rangle$', 'resultat', 'm')
save(fig, '67-102')
