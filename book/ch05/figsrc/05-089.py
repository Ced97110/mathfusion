import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(106)
box(ax,16,92,56,10,'encre',label='PGCD de 252 et 198 ?',size='m')
box(ax,2,66,34,12,'limite',label='factoriser : long',size='s',dash=True)
text(ax,19,60,'étape évitée','limite','s')
arrow(ax,(30,91.5),(19,78.5),'limite')
text(ax,67,81,'algorithme d\'Euclide','sujet','s',weight='bold')
arrow(ax,(60,91.5),(67,84),'sujet')
for i,r in enumerate([54,36,18,0]):
    y=72-11*i
    box(ax,48,y-9,38,9,'sujet',label=f'division {i+1} : reste {r}',size='s')
    if i<3: arrow(ax,(67,y-9.2),(67,y-11.8),'varie',lw=1.0)
arrow(ax,(67,77.8),(67,72.5),'sujet')
box(ax,36,2,50,10,'resultat',label='PGCD = 18',size='l')
arrow(ax,(67,29.5),(67,12.5),'resultat',lw=1.2)
text(ax,2,21,'sans factoriser','resultat','s',ha='left')
save(fig,'05-089')
