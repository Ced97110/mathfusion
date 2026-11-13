import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
cols=['4','6','8','12','16','18','20','24','28','30','⋯']
a=['4','8','12','16','20','24','28','⋯']; b=['6','12','18','24','30','⋯']; c=['12','24','36 ⋯']
cell_pos={'4':0,'6':1,'8':2,'12':3,'16':4,'18':5,'20':6,'24':7,'28':8,'30':9}
cc=4; cw=SIZE['m']*0.2124; cell=cc*cw; x0=(88-11*cell)/2
def mono(x,y,s):
    ax.text(x,y,s,color=COL['encre'],fontsize=SIZE['m'],family='DejaVu Sans Mono',ha='left',va='center',zorder=5)
def row(y,vals,role):
    s=['']*11
    for v in vals:
        i=10 if v in ('⋯','36 ⋯') else cell_pos[v]
        s[i]=v
        if v!='⋯' and v!='36 ⋯':
            ax.add_patch(Rectangle((x0+i*cell+0.4,y-3.5),cell-0.8,7,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
    mono(x0,y,''.join(f'{t:^{cc}}' for t in s))
row(56,a,'sujet'); row(38,b,'autre'); row(14,c,'resultat')
text(ax,2,64,'multiples de 4','sujet','s',ha='left')
text(ax,2,46,'multiples de 6','autre','s',ha='left')
text(ax,2,22,'nombres des deux listes','resultat','s',ha='left')
x12=x0+3.5*cell; x24=x0+7.5*cell; x36=x0+10.5*cell
arrow(ax,(x12+3,19),(x24-3,19),'varie',curve=-0.4)
arrow(ax,(x24+3,19),(x36-4,19),'varie',curve=-0.4)
text(ax,(x12+x24)/2,24.5,'+ 12','varie','s'); text(ax,(x24+x36)/2,24.5,'+ 12','varie','s')
text(ax,44,4,'le plus petit : 12','resultat','m')
save(fig,'05-127')
