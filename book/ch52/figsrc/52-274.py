import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'idéal engendré par 2','sujet','m')
text(ax,44,48,'par 5 : (2) = tout : corps','resultat','s')
for i in range(5): disc(ax,16+i*14,39,5,'resultat',label=str(i))
text(ax,44,26,'par 6 : (2) ≠ tout : pas corps','limite','s')
for i in range(6): disc(ax,12+i*12.8,16,4.6,'sujet' if i%2==0 else 'fixe',label=str(i))
text(ax,44,5,'en bleu : 0, 2, 4 seulement','sujet','s')
save(fig,'52-274')
