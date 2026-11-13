import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'pour $a=4$', 'fixe', 'm')
box(ax, 8, 42, 72, 14, 'limite', label=r'départ : $\frac{16}{0}$ n’existe pas')
arrow(ax, (44, 41), (44, 26), 'varie')
text(ax, 47, 33.5, r'$\times(a-4)=\times 0$', 'varie', 'm', ha='left')
box(ax, 8, 8, 72, 16, 'resultat', label=r'sans fraction : $16=0+16$ vrai')
save(fig, '21-130')
