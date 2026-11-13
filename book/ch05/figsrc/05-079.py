import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,52,r'$d$ prend une valeur verte','varie','m')
vals=['1','2','3','4','6','9']; ok=[1,1,1,0,1,0]
xs=[]
for i,(v,o) in enumerate(zip(vals,ok)):
    x=3.5+i*14; xs.append(x+5.5)
    box(ax,x,24,11,10,'resultat' if o else 'limite',label=v,dash=not o,size='l')
arrow(ax,(xs[0],38),(xs[4],38),'varie',curve=-0.35,both=True)
text(ax,xs[3],14,'12 seul','limite','s'); text(ax,xs[5]-2,14,'18 seul','limite','s')
save(fig,'05-079')
