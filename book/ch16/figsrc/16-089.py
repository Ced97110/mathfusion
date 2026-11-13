import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
ph=['la somme de 5 et d’un nombre','5 plus un nombre','un nombre augmenté de 5']
for i,t in enumerate(ph):
    y=60-i*13; box(ax,3,y-5,46,10,'sujet',label=t,size='s'); arrow(ax,(49.5,y),(60,30+ (1-i)*3),'varie')
box(ax,60,25,20,12,'varie',label='$+$',size='xl')
text(ax,70,43,'même signe','varie','s')
text(ax,44,13,r'$x=7$ : $7+5=12$','resultat','m')
save(fig,'16-089')
