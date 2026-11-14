import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
top=[14,24,46,56,66]; roles=['sujet']*2+['varie']*3
for x,r in zip(top,roles): box(ax,x,58,8,8,r,label='$a$')
text(ax,38,62,r'$\times$')
brace(ax,14,32,66,'sujet',label='2 facteurs',down=False)
brace(ax,46,74,66,'varie',label='3 facteurs',down=False)
bot=[20+10*i for i in range(5)]
for i,(x,r) in enumerate(zip(bot,roles)):
    box(ax,x,28,8,8,r,label='$a$')
    arrow(ax,(top[i]+4,58),(x+4,37.5),'fixe',lw=0.8)
brace(ax,20,68,28,'resultat',label=r'$a^5$ : 5 facteurs')
save(fig,'14-021')
