import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,56,'sin² x + cos² x = 1','sujet','l')
w1=48; w2=16; x0=12
box(ax,x0,34,w1,10,'sujet',label='cos² x'); box(ax,x0+w1,34,w2,10,'varie',label='sin² x')
brace(ax,x0,x0+w1+w2,45,'fixe','1',down=False)
box(ax,x0,10,w1,10,'resultat',label='cos² x'); box(ax,x0+w1,10,w2,10,'varie',fill=False,label='sin² x',dash=True)
brace(ax,x0,x0+w1,8,'resultat','= 1 − sin² x')
save(fig,'32-112')
