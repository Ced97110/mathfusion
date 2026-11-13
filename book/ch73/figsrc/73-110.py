import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,13,57,'élément','encre','s'); text(ax,39,57,'couple de départ','encre','s'); text(ax,73,57,'résultat','encre','s')
rows=[(40,'(I, 0)','sujet','(A, 0)\ninchangé','resultat'),(14,'(I, x)','limite','(A, x)\nmodifié','limite')]
for y,a,ra,res,rr in rows:
    box(ax,2,y,22,14,ra,label=a,size='m'); text(ax,27.5,y+7,'×','encre','l')
    box(ax,31,y,16,14,'fixe',label='(A, 0)',size='m'); text(ax,52,y+7,'=','encre','l')
    box(ax,57,y,28,14,rr,label=res,size='s')
text(ax,44,5,r'$x=(2\,;\,0)$ ; A : quart de tour','fixe','s')
save(fig,'73-110')
