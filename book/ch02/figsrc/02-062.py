import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
u=0.93; xa=4; xb=xa+43*u; xc=xb+16*u; xe=xc+27*u
for y in (58,30):
    for (x0,x1,s) in ((xa,xb,'a = 43'),(xb,xc,'b = 16'),(xc,xe,'c = 27')):
        box(ax,x0,y,x1-x0,6,'sujet',label=s,size='s')
for x,r in ((xb,'fixe'),(xc,'fixe'),(xa,'resultat'),(xe,'resultat')): line(ax,[(x,36),(x,58)],r,lw=0.5,dash=True)
text(ax,24,47,'mêmes bandes, même ordre','fixe','s')
brace(ax,xa,xc,65.5,'varie',label='a + b = 59',down=False)
line(ax,[(xc,56),(xc,66)],'varie',lw=1.6)
brace(ax,xb,xe,28.5,'varie',label='b + c = 43',down=True)
line(ax,[(xb,28),(xb,38)],'varie',lw=1.6)
text(ax,44,78,'(43 + 16) + 27 = 86','resultat','m'); text(ax,44,16,'43 + (16 + 27) = 86','resultat','m')
text(ax,44,7,'seul l’arrêt change','varie','m')
save(fig,'02-062')
