import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def rangee(y, titre, poly, labels, n, role):
    text(ax, 4, y + 12, titre, 'sujet', 'm', ha='left')
    text(ax, 84, y + 12, poly, 'encre', 'm', ha='right')
    w = 14; gap = 3; x0 = 4
    for i, lab in enumerate(labels):
        box(ax, x0 + i * (w + gap), y, w, 8, role, label=lab, size='m')
    xe = x0 + n * (w + gap) - gap
    brace(ax, x0, xe, y - 1.5, 'fixe', label=f'$n={n}$ éléments', down=True, depth=1.4)
rangee(36, r'$u=\sqrt{2}$', r'$f=\lambda^2-2$', ['$1$', r'$\sqrt{2}$'], 2, 'resultat')
rangee(8, r'$u=\sqrt[3]{2}$', r'$f=\lambda^3-2$', ['$1$', '$u$', '$u^2$'], 3, 'resultat')
save(fig, '77-090')
