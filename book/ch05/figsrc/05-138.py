import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(82)
def bar(y,x,l,role,lab):
    rect(ax,26,y,l,5,role); text(ax,24,y+2.5,lab,role,'s',ha='right')
text(ax,44,77,'90 divise 630 : ça marche','resultat','m')
s=0.09
bar(67,26,90*s,'sujet','90'); bar(59.5,26,630*s,'autre','630')
bar(52,26,90*s,'resultat','PGCD 90'); bar(44.5,26,630*s,'resultat','PPCM 630')
line(ax,[(2,40),(86,40)],'fixe',dash=True)
text(ax,44,35,'12 et 18 : pas de division','limite','m')
s=1.3
bar(27,26,12*s,'sujet','12'); bar(19.5,26,18*s,'autre','18')
bar(12,26,6*s,'limite','PGCD 6'); bar(4.5,26,36*s,'limite','PPCM 36')
text(ax,26+6*s+2.5,14.5,r'$\neq 12$','limite','s',ha='left')
text(ax,26+36*s+2.5,7,r'$\neq 18$','limite','s',ha='left')
save(fig,'05-138')
