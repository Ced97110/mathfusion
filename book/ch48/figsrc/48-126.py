import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$G/N$ : 6 paquets','encre','m',weight='bold')
text(ax,16,46,r'$H/N$','sujet','s')
G=[['0, 6','3, 9'],['1, 7','4, 10'],['2, 8','5, 11']]; S=['0, 3, 6, 9','1, 4, 7, 10','2, 5, 8, 11']
for g in range(3):
    x0=4+g*28; r='sujet' if g==0 else 'autre'
    for k in range(2): box(ax,x0+k*13,32,11,10,r,label=G[g][k],size='s')
    brace(ax,x0,x0+24,31,r,label=S[g])
text(ax,44,16,'regroupés 2 par 2','fixe','s')
text(ax,44,8,r'$G/H$ : 3 paquets','resultat','m',weight='bold')
save(fig,'48-126')
