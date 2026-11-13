import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
xs=[16+9*i for i in range(7)]
for i,(x,d) in enumerate(zip(xs,'0148422')):
    if i==0: box(ax,x,64,8,8,'sujet',fill=False,dash=True,label=d,size='l')
    elif i==1: box(ax,x,64,8,8,'varie',label=d,size='l')
    else: box(ax,x,64,8,8,'fixe',label=d,size='l')
text(ax,20,75.5,'0 imaginé','sujet','s')
text(ax,29,60.5,'témoin : 1 < 5','varie','s')
f=lambda v: 8+v/1e6*72
line(ax,[(8,40),(80,40)],'fixe')
for v,l in ((0,'0'),(1e6,'1 000 000')):
    line(ax,[(f(v),38.8),(f(v),41.2)],'fixe',lw=0.8); text(ax,f(v),36.6,l,'fixe','s')
disc(ax,f(148422),40,1.2,'sujet')
brace(ax,8,18.4,42,'resultat','148 422',down=False)
brace(ax,19,80,42,'fixe','851 578',down=False)
disc(ax,8,40,1.6,'resultat')
text(ax,44,26,'arrondi au million : 0','resultat','m')
save(fig,'01-113')
