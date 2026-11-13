import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
cs=8; gx,gy=4,40
for a in range(5):
    for b in range(5):
        box(ax,gx+cs*a+0.4,gy+cs*b+0.4,cs-0.8,cs-0.8,'limite' if a==b==0 else 'resultat',r=0.5)
text(ax,gx+cs/2,gy+cs/2,'0 ; 0','limite','s')
text(ax,gx+20,gy-3.5,r'$a$','encre','m'); text(ax,1.8,gy+20,r'$b$','encre','m')
box(ax,52,68,6,6,'limite'); text(ax,60,71,'couple interdit','limite','m',ha='left')
box(ax,52,56,6,6,'resultat'); text(ax,60,59,'PGCD existe','resultat','m',ha='left')
text(ax,4,31,'diviseurs communs de 0 et 0','encre','m',ha='left')
for i,t in enumerate(['1','2','3','4']): box(ax,4+i*15,14,12,10,'sujet',label=t)
box(ax,64,14,12,10,'limite',fill=False,dash=True,label='…')
text(ax,4,7,"aucun n'est le plus grand",'limite','m',ha='left')
save(fig,'05-153')
