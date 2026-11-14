import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 8, 66, 72, 10, 'fixe', label=r'$\mathbb{F}_{q^n}=\mathbb{F}_8$ ($q=2$, $n=3$) existe')
arrow(ax, (44, 66), (44, 59), 'fixe')
for k in range(7):
    x = 13 + 11 * k
    lab = r'$\alpha$' if k == 0 else rf'$\alpha^{k + 1}$'
    disc(ax, x, 53, 3.8, 'sujet', label=lab, size='s')
brace(ax, 9, 83, 48, 'sujet', label='les 7 éléments non nuls')
arrow(ax, (44, 40), (44, 33), 'varie')
text(ax, 48, 36.5, r'$\alpha$ est racine de', 'varie', 's', ha='left')
box(ax, 10, 22, 68, 10, 'resultat', label=r'$x^3+x+1$ : irréductible, degré 3')
arrow(ax, (44, 22), (44, 15), 'resultat')
box(ax, 24, 5, 40, 10, 'sujet', label=r'$N(3,2)\geq 1$', weight='bold')
save(fig, '67-122')
