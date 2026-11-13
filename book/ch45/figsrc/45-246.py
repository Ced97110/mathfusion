import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def row(y,vals,role,label):
    text(ax,2,y+6,label,role,'s',ha='left')
    for i,v in enumerate(vals): box(ax,42+i*14,y-3,10,9,role,label=str(v),size='l')
row(52,[1,2,3],'fixe','départ')
row(30,[3,2,1],'sujet','échange puis décalage')
row(10,[1,3,2],'autre','décalage puis échange')
text(ax,85,22,'≠','limite','xl',weight='bold')
text(ax,44,63,'deux ordres, deux résultats','limite','s')
save(fig,'45-246')
