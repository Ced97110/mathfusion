import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 18, 76, 'les 4 règles du module', 'sujet', 's', weight='bold')
text(ax, 70, 76, r'les 4 exigences sur $\eta$', 'autre', 's', weight='bold')
rows = [(55, r'$a(x+y)=ax+ay$', r'$\eta(a)$ est un' + '\nendomorphisme'),
        (39, r'$(a+b)x=ax+bx$', r'$\eta$ respecte' + '\nla somme'),
        (23, r'$(ab)x=a(bx)$', r'$\eta$ respecte' + '\nle produit'),
        (7, r'$1x=x$', r'$\eta$ envoie 1 sur' + "\n« ne rien changer »")]
for k, (y, l, r) in enumerate(rows, start=1):
    yc = y + 6
    box(ax, 2, y, 33, 12, 'sujet', label=l, size='s')
    box(ax, 53, y, 33, 12, 'autre', label=r, size='s')
    disc(ax, 44, yc, 3.6, 'resultat', label=str(k), size='m')
    arrow(ax, (35.5, yc), (40, yc), 'resultat', lw=1.6)
    arrow(ax, (48, yc), (52.5, yc), 'resultat', lw=1.6)
save(fig, '57-081')
