import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
cols='ABCD'
rows=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for c,l in enumerate(cols):
    text(ax,34+8*c,84,l,'fixe','m')
for r,(a,b) in enumerate(rows):
    y=72-8*r
    for c in range(4):
        if c in (a,b): box(ax,30+8*c,y,8,8,'sujet')
        else: box(ax,30+8*c,y,8,8,'fixe',fill=False)
    text(ax,22,y+4,cols[a]+cols[b],'sujet','s')
line(ax,[(66,32),(66,80)],'resultat',lw=1.0)
line(ax,[(64.5,32),(66,32)],'resultat',lw=1.0)
line(ax,[(64.5,80),(66,80)],'resultat',lw=1.0)
text(ax,76,56,'6 choix','resultat','m')
text(ax,44,24,r'$\binom{4}{2}$ = 6','resultat','l')
text(ax,44,15,'ligne 4 : 1, 4, 6, 4, 1','encre','s')
text(ax,44,7,r'coefficient de $a^{2}b^{2}$ : 6','encre','s')
save(fig,'01-182')
