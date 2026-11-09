def vv(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    vv(list,idx+1)
app=["ints","edis","yt"]
vv(app)