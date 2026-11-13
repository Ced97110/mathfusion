import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
cols=[20,31,46,57]
w=9
lab={'A':'exposants du 2 :\n2 et 1 → garde 1','B':'exposants du 3 :\n1 et 2 → garde 1'}
lab={'A':'exposants du 2 :\n'+r'2 et 1 $\rightarrow$ garde 1','B':'exposants du 3 :\n'+r'1 et 2 $\rightarrow$ garde 1'}
text(ax,(cols[0]+cols[1]+w)/2,64,lab['A'],'encre','s')
text(ax,(cols[2]+cols[3]+w)/2,64,lab['B'],'encre','s')
text(ax,4,44,'12 =','encre','m',ha='left'); text(ax,4,28,'18 =','encre','m',ha='left')
def b(c,y,l,role,dash=False): box(ax,c,y,w,10,role,label=l,dash=dash)
b(cols[0],39,'2','resultat'); b(cols[1],39,'2','fixe',True); b(cols[2],39,'3','resultat')
b(cols[0],23,'2','resultat'); b(cols[2],23,'3','resultat'); b(cols[3],23,'3','fixe',True)
line(ax,[(cols[0]+w/2,38),(cols[0]+w/2,34)],'resultat'); line(ax,[(cols[2]+w/2,38),(cols[2]+w/2,34)],'resultat')
text(ax,44,10,r'$2 \times 3 = 6$','resultat','xl',weight='bold')
save(fig,'05-075')
