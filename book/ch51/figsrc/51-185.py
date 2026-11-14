import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
box(ax,2,22,36,40,'fixe')
text(ax,20,57,'anneau connu','fixe','s')
box(ax,8,28,24,18,'sujet',label=r'$S$ : à tester',size='s')
text(ax,64,65,'3 contrôles','varie','s')
for y,l in zip((50,38,26),(r'$1\in S$',r'$a-b\in S$',r'$a\cdot b\in S$')):
    box(ax,46,y,36,9,'varie',label=l,size='m')
box(ax,2,2,40,14,'resultat',label='tous réussis :\nhuit règles héritées',size='s')
box(ax,46,2,40,14,'limite',label='un contrôle échoue :\npas de conclusion',size='s')
arrow(ax,(46,24),(36,17),'resultat'); arrow(ax,(80,24),(80,17),'limite')
save(fig,'51-185')
