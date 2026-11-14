import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = [(66, 'sujet', 'Départ', r'$a/b=3{,}2-0{,}6\,i$', 'erreurs d’arrondi : $0{,}2$ et $0{,}4$'),
         (38, 'varie', 'Étape : factoriser', r'$r=b\times(\mathrm{erreurs})$', r'$\delta(r)=5\times(0{,}2^2+0{,}4^2)$'),
         (10, 'resultat', 'Arrivée', r'$\delta(r)=5\times 0{,}2=1$', r'$1<5=\delta(b)$')]
for y, role, head, l1, l2 in steps:
    box(ax, 4, y, 80, 20, role)
    text(ax, 8, y + 16, head, role, 's', ha='left', weight='bold')
    text(ax, 44, y + 9.5, l1, role, 'm')
    text(ax, 44, y + 3.8, l2, role, 's')
arrow(ax, (44, 66), (44, 58), 'fixe')
arrow(ax, (44, 38), (44, 30), 'fixe')
save(fig, '56-130')
