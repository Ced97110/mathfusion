import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,'images de ℤ = quotients de ℤ','sujet','s')
box(ax,3,25,14,12,'sujet',label='ℤ',size='l')
for i,(n,q) in enumerate([(2,'ℤ/2ℤ'),(3,'ℤ/3ℤ'),(6,'ℤ/6ℤ')]):
    y=44-i*18
    box(ax,62,y,24,10,'resultat',label=q,size='m')
    arrow(ax,(17,31),(62,y+5),'varie')
    text(ax,40+ (0),y+5+ (31-(y+5))*0.0+3.2 - (31-(y+5))*0.0,f'idéal {n}ℤ','varie','s') if False else None
    xm=39.5; ym=31+(y+5-31)*0.5
    text(ax,xm,ym+2.6,f'idéal {n}ℤ','varie','s')
text(ax,44,5,'les idéaux de ℤ : les multiples d’un nombre','fixe','s')
save(fig,'52-163')
