import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def uc(ax,cx,cy,R,e=4):
    disc(ax,cx,cy,R,"fixe",fill=False)
    line(ax,[(cx-R-e,cy),(cx+R+e,cy)],"fixe",lw=0.6); line(ax,[(cx,cy-R-e),(cx,cy+R+e)],"fixe",lw=0.6)
fig,ax=canvas(76); cx,cy,R=26,38,19; uc(ax,cx,cy,R)
for y,lab,pl in [(cy+R,"tan 90° = 1 ÷ 0","(0, 1)"),(cy-R,"tan 270° = −1 ÷ 0","(0, −1)")]:
    disc(ax,cx,y,1.5,"sujet"); line(ax,[(cx,cy),(cx,y)],"sujet",lw=1.0)
    line(ax,[(cx+3,y),(53,y)],"limite",lw=0.7,dash=True)
    text(ax,cx-3,y+(3 if y>cy else -3),pl,"sujet",ha="right")
    text(ax,70,y,lab,"limite","m")
text(ax,70,cy,"on ne divise\npas par 0","limite","m")
save(fig,"28-135")
