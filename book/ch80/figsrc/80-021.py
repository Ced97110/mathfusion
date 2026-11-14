import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,48,61,'nombres\nordinaires','sujet','s'); text(ax,74,61,'alarme\n(0 et 1)','autre','s')
text(ax,18,40,r'$x\times x=x$ ?','encre','m'); text(ax,18,20,'ordre dans\nl’addition ?','encre','s')
box(ax,36,33,24,14,'limite',label='2 × 2 = 4\nfaux',size='s'); box(ax,62,33,24,14,'resultat',label='0 et 1\nvrai',size='s')
box(ax,36,13,24,14,'resultat',label='vrai',size='s'); box(ax,62,13,24,14,'fixe',label='peut rester\nvraie',size='s')
text(ax,44,5,'règle par règle : vraie ou fausse ?','encre','s')
save(fig,'80-021')
