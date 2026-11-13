import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,30,60,22,7,'fixe',label='0! = 1')
text(ax,14,63.5,'départ posé','fixe','s')
line(ax,[(21.5,63.5),(29.5,63.5)],'fixe',lw=0.6)
ys=[51,42,33,24,15]
labs=['1! = 1','2! = 2','3! = 6','4! = 24','5! = 120']
for y,l in zip(ys,labs): box(ax,30,y,22,7,'resultat',label=l)
mids=[63.5]+[y+3.5 for y in ys]
for i in range(5):
    arrow(ax,(52.5,mids[i]),(52.5,mids[i+1]),'varie',curve=0.4)
    text(ax,61,(mids[i]+mids[i+1])/2,f'× {i+1}','varie','s',ha='left')
text(ax,44,6,'(n + 1)! = (n + 1) × n!','varie','m')
save(fig,'01-055')
