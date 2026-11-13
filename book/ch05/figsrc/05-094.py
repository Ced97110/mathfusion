import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
y=76
text(ax,20,y,'dernier','varie',14,weight='bold'); text(ax,46,y,r'$r$','sujet',16); text(ax,68,y,r'$\neq0$','limite',16)
text(ax,20,y-12,'le plus tardif','varie','s'); text(ax,46,y-12,'un reste','sujet','s'); text(ax,68,y-12,'écarte le reste nul','limite','s')
text(ax,2,50,'restes de 252 ÷ 198 :','encre','s',ha='left')
cols=[14,34,54,74]
for c,r in zip(cols,[54,36,18,0]):
    role='resultat' if r==18 else ('limite' if r==0 else 'fixe')
    box(ax,c-8,34,16,10,role,label=str(r),size='l',lw=1.6 if r==18 else 0.8)
arrow(ax,(26,62),(50,45.5),'varie',curve=0.15)
arrow(ax,(74,62),(74,45.5),'limite')
box(ax,24,6,40,10,'resultat',label='on lit : 18',size='l')
arrow(ax,(54,33.5),(54,16.5),'resultat',lw=1.4)
text(ax,74,28,'jamais lu','limite','s')
save(fig,'05-094')
