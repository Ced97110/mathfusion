import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(50); x0=8; W1=72
text(ax,44,43,r"$\sin^2\theta+\cos^2\theta=1$","encre","l")
box(ax,x0,18,W1*0.25,10,"sujet"); box(ax,x0+W1*0.25,18,W1*0.75,10,"varie")
text(ax,x0+W1*0.125,33,"sin² 30° = 0,25","sujet","s",ha="center")
text(ax,x0+W1*0.625,33,"cos² 30° = 0,75","varie","m")
brace(ax,x0,x0+W1,16,"resultat","somme = 1")
save(fig,"28-143")
