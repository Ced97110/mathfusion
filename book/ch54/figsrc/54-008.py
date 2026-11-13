import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
for i, (nm, v, xx) in enumerate([(r'$a_0$', '1', 14), (r'$a_1$', '1', 38), (r'$a_2$', '−2', 62)]):
    text(ax, xx + 8, 84, nm, 'sujet', 'm')
    box(ax, xx, 70, 16, 10, 'sujet', label=v, size='l')
text(ax, 44, 60, r'avec $x=1$ : $1+1-2=0$', 'varie', 'm')
arrow(ax, (36, 57), (23, 46), 'varie')
text(ax, 23, 50, 'refusé', 'limite', 's', ha='right')
text(ax, 64, 50, 'retenu', 'resultat', 's', ha='left', weight='bold')
box(ax, 4, 20, 38, 24, 'limite', label='$x=1$ : calcul nul\nmais les $a_i$ ne\nsont pas tous nuls', size='s')
box(ax, 46, 14, 38, 34, 'resultat', lw=1.8, label='$x$ sans propriété :\n$a_0+a_1x+a_2x^2=0$\nseulement si tous\nles $a_i$ sont nuls', size='s', weight='bold')
arrow(ax, (44, 31), (46, 31), 'resultat', both=False)
text(ax, 44, 6, 'la règle retenue pour $x$ est la boîte verte', 'resultat', 's')
save(fig, '54-008')
