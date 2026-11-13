import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,54,'10² = 100 : deux zéros','fixe','m')
text(ax,44,47,'10³ = 1 000 : trois zéros','fixe','m')
text(ax,44,39.5,'+1 facteur 10 → +1 zéro','varie','s')
arrow(ax,(78,52),(78,46),'varie')
text(ax,11,24,'10⁶ =','sujet','l')
# sept cases de 8 mm, pas de 9 mm : 1 suivi de six zéros
for i in range(7):
    x=20+9*i
    if i==0: box(ax,x,20,8,8,'fixe',label='1',size='m')
    else: box(ax,x,20,8,8,'resultat',label='0',size='m')
brace(ax,29,82,19,'resultat',label='6 zéros',down=True,size='s')
arrow(ax,(14.5,20),(49,13.5),'varie',curve=0.2)
text(ax,44,6,'exposant 6 = nombre de zéros','sujet','s')
save(fig,'04-084')
