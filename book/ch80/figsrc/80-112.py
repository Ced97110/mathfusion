import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,6,64,76,12,'sujet',label='isomorphisme de treillis',size='m')
box(ax,6,44,76,12,'fixe',label=r'configuration : $e_1,\ e_2,\ e_3$',size='m')
box(ax,6,22,76,14,'varie',label="$(a+b)'=a'+b'$",size='l',lw=1.6)
box(ax,6,3,76,12,'resultat',label='application semi-linéaire',size='m')
for y in (64,44,22): arrow(ax,(44,y),(44,y-8),'fixe')
text(ax,66,40,'étape décisive','varie','s')
save(fig,'80-112')
