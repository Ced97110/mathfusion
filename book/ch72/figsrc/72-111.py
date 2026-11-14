import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
box(ax,22,60,44,9,'sujet',label=r'$e_3=(0,0,1)$',size='l')
text(ax,44,56,'donne 0 avec chaque y','resultat','s')
rows=[('(3, 4, 5)',44,False),('(1, 1, 1)',32,False),('(7, 2, 9)',20,False),('y quelconque',8,True)]
for lab,y,d in rows:
    box(ax,8,y,28,8,'autre',label=(r'$y=$'+lab if not d else 'y quelconque'),size='s',dash=d)
    arrow(ax,(38,y+4),(52,y+4),'fixe')
    box(ax,54,y,26,8,'resultat',label=r'$B(e_3,y)=0$',size='s',dash=d)
save(fig,'72-111')
