import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(62)
text(ax,44,56,'3/4 = 9/12','resultat','l')
for g in range(4):
    row(ax,12+g*16.5,24,5,9,['sujet']*3 if g<3 else [None]*3)
brace(ax,12,60,33,'sujet','3 quarts × 3 = 9',down=False)
brace(ax,12,27,24,'sujet','12 ÷ 4 = 3 par quart')
save(fig,'07-030')
