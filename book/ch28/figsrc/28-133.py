import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(86); cx,cy,R=44,52,27; uc(ax,cx,cy,R)
for d in range(0,360,15):
    if d%30==0 and d%90!=0 or d%90==0 or d%45==0 and d%30!=0:
        x,y=pt(cx,cy,R,d)
        role="fixe" if d%90==0 else ("varie" if d%90==45 else "sujet")
        disc(ax,x,y,1.5,role)
disc(ax,6,19,1.5,"sujet"); text(ax,10,19,"12 points : a, b, c + signe","encre","s",ha="left")
disc(ax,6,13,1.5,"fixe"); text(ax,10,13,"4 points sur les axes : 0, ±1","encre","s",ha="left")
text(ax,17,5,r"$a=0{,}5$","sujet"); text(ax,44,5,r"$b\approx0{,}707$","varie"); text(ax,72,5,r"$c\approx0{,}866$","sujet")
save(fig,"28-133")
