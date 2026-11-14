import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,2,58,40,10,'autre',label='sous-groupe normal',size='s'); box(ax,46,58,40,10,'sujet',label='idéal',size='s')
box(ax,2,44,40,10,'fixe',label='1 opération : +',size='s'); box(ax,46,44,40,10,'fixe',label='2 opérations : + et ×',size='s')
box(ax,2,30,40,10,'autre',label=r'$3+8-3=8\in 4\mathbb{Z}$',size='s'); box(ax,46,30,40,10,'sujet',label=r'$3+8-3=8\in 4\mathbb{Z}$',size='s')
box(ax,2,16,40,10,'fixe',fill=False,dash=True,label='pas de second produit',size='s'); box(ax,46,16,40,10,'sujet',label=r'$8\times 3=24\in 4\mathbb{Z}$',size='s')
box(ax,14,1,60,10,'resultat',label='même rôle : définir un quotient',size='s')
save(fig,'52-045')
