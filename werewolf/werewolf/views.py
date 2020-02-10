from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
import random

# mysql> create table version-1 ( gameid SMALLINT NOT NULL primarykey ,
#     -> lobbystatus SMALLINT,
#     -> playerid SMALLINT,
#     -> alias varchar(30),
#     -> role SMALLINT,
#     -> alive SMALLINT,
#     -> status SMALLINT,
#     -> team SMALLINT);

def lobby(request):
    cnx = mysql.connector.connect(host='106.14.189.3', port='3306', user='root',\
                                  passwd='L18_jhk123qwe',database='werewolf')
    cursor = cnx.cursor()
    query = ("SELECT gameid, alias FROM v1 WHERE lobbystatus = 1")
    cursor.execute(query)
   # playercount = str(1)
    idlst = [0,0,0,0,0]
    aliasLst=[0,0,0,0,0]
    i = 0
    for (gameid, alias) in cursor:
        idlst[i] = (gameid)
        aliasLst[i] = (alias)
        i += 1

    for i in range(5):
        if idlst[i] == 0:
            idlst[i] = "/"
            aliasLst[i] = "/"

    return render(request, 'lobby.html',{ \
                  'id0': idlst[0], 'alias0': aliasLst[0], \
                  'id1': idlst[1], 'alias1': aliasLst[1], \
                  'id2': idlst[2], 'alias2': aliasLst[2], \
                  'id3': idlst[3], 'alias3': aliasLst[3], \
                  'id4': idlst[4], 'alias4': aliasLst[4]} )

def signin(request):
    return render(request, 'room-sign-in.html')

def create(request):
    cnx = mysql.connector.connect(host='106.14.189.3', port='3306', user='root', \
                                  passwd='L18_jhk123qwe', database='werewolf')
    cursor = cnx.cursor()
    keystr= "gameid, lobbystatus, playerid, alias"
    #gameid = random.random(9999)
    gamestr = str(random.randrange(9999))

    alias = request.GET['alias']
    valuestr = gamestr + ',' + "1, " + "1, " + '"' + alias + '"'
    cursor.execute("insert into v1(" + keystr + ") VALUES(" + valuestr + ");")
    cnx.commit()

    cursor.close()
    cnx.close()
    return render(request,'room.html')