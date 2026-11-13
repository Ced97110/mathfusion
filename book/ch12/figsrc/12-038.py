import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,20,47,'gauche','sujet','m'); text(ax,68,47,'droite','autre','m')
for y,b,r,t in [(28,8,'resultat','vrai'),(8,5,'limite','faux')]:
    box(ax,8,y-1,24,14,'sujet',label='8',size='l')
    text(ax,44,y+6,r'$=$',r,'xl')
    box(ax,56,y-1,24,14,'autre',label=str(b),size='l')
    text(ax,44,y-3,t,r,'m')
save(fig,'12-038')
