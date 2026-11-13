import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
s=0.12; b=0.25; L=36; x0=24; t=3
for hh in (0,100,200):
    y=10+hh*s; sh=b*hh*s
    if hh: poly(ax,[(x0,y),(x0+L,y),(x0+L,y+t),(x0,y+t)],'fixe',fill=False)
    poly(ax,[(x0+sh,y),(x0+sh+L,y),(x0+sh+L,y+t),(x0+sh,y+t)],'sujet')
    if hh: arrow(ax,(x0+L,y+t/2),(x0+L+sh,y+t/2),'varie')
    text(ax,x0-3,y+t/2,f'hauteur {hh}','fixe','s',ha='right')
    text(ax,x0+L+sh+3,y+t/2,f'glisse de {b*hh:g} px'.replace('.',','),'varie','s',ha='left')
text(ax,24,48,r'$b$ = 0,25','sujet')
text(ax,62,48,r'glissement = $b \times y$','resultat')
save(fig,'73-003')
