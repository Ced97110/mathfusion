import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
u=9; x0=3.5
def row(y,seq):
    x=x0
    for k in seq:
        if k=='a': box(ax,x,y,u,11,'sujet',label=r'$a$',size='s'); x+=u
        else: box(ax,x,y,2*u,11,'varie',label=r'$b$',size='s'); x+=2*u
row(46,list('abababab'[:6]))
row(19,list('aaabbb'))
text(ax,8,38,'=','resultat','xl',weight='bold'); text(ax,50,38,r'$ab=ba$ : on échange','resultat','s')
brace(ax,x0,x0+9*u,18,'resultat',label='9 quarts',down=True)
text(ax,20,3,r'$a$ : 1 quart','sujet','s'); text(ax,66,3,r'$b$ : 2 quarts','varie','s')
save(fig,'45-134')
