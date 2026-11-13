import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,46,56,'on multiplie de 1 au nombre','fixe','s')
rows=[('factorielle de 4','4×3×2×1','= 24',43),('factorielle de 5','5×4×3×2×1','= 120',31),('factorielle de 10','10×9×8×7×6×5×4×3×2×1','= 3 628 800',19)]
fig.canvas.draw(); rd=fig.canvas.get_renderer()
for nom,prod,res,y in rows:
    box(ax,3,y,26,7,'sujet',label=nom,size='s')
    t=text(ax,34,y+3.5,prod,'fixe','s',ha='left')
    bb=t.get_window_extent(rd); wmm=bb.width/fig.dpi*25.4
    box(ax,33,y,wmm+2,7,'fixe',fill=False,r=0.8)
    arrow(ax,(33,y+3.5),(29.5,y+3.5),'varie',lw=0.8)
    text(ax,85,y+3.5,res,'resultat','s',ha='right')
brace(ax,34,61,18,'limite',label='10 facteurs à recopier')
text(ax,16,12,'deux mots suffisent','sujet','s')
save(fig,'01-051')
