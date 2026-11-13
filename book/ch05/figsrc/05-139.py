import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(80)
text(ax,44,77,'PGCD × PPCM = 6 × 36 = 216','resultat','m')
c=9
for k in range(6): rect(ax,8+k*c,58,c,c,'resultat')
text(ax,4.5,62.5,'6','resultat','s'); text(ax,8+27,70,'36','resultat','s')
text(ax,66,62.5,'6 carrés','resultat','s',ha='left')
text(ax,44,50,'12 × 18 = 216','sujet','m')
for i in range(3):
    for j in range(2): rect(ax,8+i*c,24+j*c,c,c,'sujet')
text(ax,4.5,33,'12','sujet','s'); text(ax,8+13.5,44.5,'18','sujet','s')
text(ax,40,33,'6 carrés','sujet','s',ha='left')
text(ax,44,14,'côté d\'un carré = PGCD = 6','encre','s')
save(fig,'05-139')
