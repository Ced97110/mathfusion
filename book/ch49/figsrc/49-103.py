import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,2,62,r'$g_1$ et $g_2$ : quarts de tour','fixe','s',ha='left')
text(ax,63,56,'images de 1, 2, 3, 4','fixe','s')
def ligne(y,role,lab,sub,vals):
    text(ax,2,y+6.5,lab,role,'s',ha='left')
    if sub: text(ax,2,y+2,sub,role,'s',ha='left')
    box(ax,38,y,48,9,role,label='     '.join(vals),size='m')
ligne(40,'varie',r'$T(g_1)\circ T(g_2)$',r"$g_2$ agit d'abord",'3412')
ligne(24,'sujet',r'$T(g_1g_2)$',None,'3412')
text(ax,62,36.5,'=','resultat','l',weight='bold')
ligne(5,'fixe',r'$T(1)$ : le neutre','chaque point reste','1234')
save(fig,'49-103')
