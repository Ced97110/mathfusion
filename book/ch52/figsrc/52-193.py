import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
s=3.4; x0=9; x1=x0+20*s
for y,step,role,lab in [(38,4,'sujet','pas de 4'),(24,5,'autre','pas de 5')]:
    for i in range(20//step):
        box(ax,x0+i*step*s,y,step*s,6,role)
    text(ax,x0+2,y+9,lab,role,'s',ha='left')
box(ax,x0,8,20*s,6,'resultat',label='multiple de 4 et de 5',size='s')
for x in (x0,x1): line(ax,[(x,6),(x,50)],'fixe',dash=True)
brace(ax,x0,x1,50,'varie',label=r'$39-19=20$',down=False)
text(ax,x0,3,'0','fixe','s'); text(ax,x1,3,'20','fixe','s')
save(fig,'52-193')
