import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(62)
x0=36; c=9
for i in range(2): rect(ax,x0+i*c,38,c,c,'sujet')
rect(ax,x0+2*c,38,c,c,'autre')
brace(ax,x0,x0+2*c,48,'sujet',label=r'$s$',down=False)
brace(ax,x0+2*c,x0+3*c,48,'autre',label=r'$t$',down=False)
text(ax,2,42.5,'exposants\ndans $a$ et $b$','encre','s',ha='left')
rect(ax,x0,12,c,c,'resultat'); rect(ax,x0+c,12,2*c,c,'resultat')
brace(ax,x0,x0+c,12,'resultat',label='plus petit')
brace(ax,x0+c,x0+3*c,12,'resultat',label='plus grand')
text(ax,2,16.5,'exposants dans\nPGCD et PPCM','encre','s',ha='left')
for x in (x0,x0+3*c): line(ax,[(x,23),(x,37)],'fixe',dash=True)
text(ax,x0+1.5*c,30,r'même total : $s+t$','varie','s')
text(ax,66,42.5,r'$s=2$, $t=1$','encre','s',ha='left')
save(fig,'05-140')
