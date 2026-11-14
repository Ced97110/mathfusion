import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,'Klein : 4, normal','sujet','m')
for k,l in enumerate(['id','(12)(34)','(13)(24)','(14)(23)']): box(ax,4+20*k,36,19,9,'sujet',label=l,size='s')
for r_ in (22,11):
    for k in range(4): box(ax,4+20*k,r_,19,9,'fixe',label='cycle',size='s')
text(ax,44,4,r'donc $A_4$ n’est pas simple','limite','m')
save(fig,'73-180')
