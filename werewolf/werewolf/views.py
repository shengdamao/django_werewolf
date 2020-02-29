from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
import random
import datetime


# mysql> CREATE TABLE v2 (
#     room SMALLINT NOT NULL PRIMARY KEY,
#     createdTime DATETIME NOT NULL,
#     expiredTime DATETIME NOT NULL,
#     alias VARCHAR(32) NOT NULL,
#     masterKey VARCHAR(32) NOT NULL,
#     lobbyStatus SMALLINT NOT NULL,
#     isInvisible SMALLINT,
#     totalGames SMALLINT,
#     pwd VARCHAR(20));


def lobby(request):
    cnx = mysql.connector.connect(host='106.14.189.3', port='3306', user='root', \
                                  passwd='L18_jhk123qwe', database='werewolf')
    cursor = cnx.cursor()
    query = ("SELECT gameid, alias FROM v1 WHERE lobbystatus = 1")

    cursor.execute(query)
    # playercount = str(1)
    idlst = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    aliasLst = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    for (gameid, alias) in cursor:
        idlst[i] = (gameid)
        aliasLst[i] = (alias)
        i += 1

    for i in range(9):
        if idlst[i] == 0:
            idlst[i] = "/"
            aliasLst[i] = "/"

    return render(request, 'lobby.html', { \
        'id0': idlst[0], 'alias0': aliasLst[0], \
        'id1': idlst[1], 'alias1': aliasLst[1], \
        'id2': idlst[2], 'alias2': aliasLst[2], \
        'id3': idlst[3], 'alias3': aliasLst[3], \
        'id4': idlst[4], 'alias4': aliasLst[4], \
        'id5': idlst[5], 'alias5': aliasLst[5], \
        'id6': idlst[6], 'alias6': aliasLst[6], \
        'id7': idlst[7], 'alias7': aliasLst[7], \
        'id8': idlst[8], 'alias8': aliasLst[8] \
        })


def signin(request):
    return render(request, 'room-sign-in.html')


# mysql> CREATE TABLE v2 (
#     room SMALLINT NOT NULL PRIMARY KEY,
#     createdTime DATETIME NOT NULL,
#     expiredTime DATETIME NOT NULL,
#     alias VARCHAR(32) NOT NULL,
#     masterKey VARCHAR(32) NOT NULL,
#     lobbyStatus SMALLINT NOT NULL,
#     isInvisible SMALLINT,
#     totalGames SMALLINT,
#     pwd VARCHAR(20));


def create(request):
    cnx = mysql.connector.connect(host='106.14.189.3', port='3306', user='root', \
                                  passwd='L18_jhk123qwe', database='werewolf')
    cursor = cnx.cursor()

    keystr = "room, createdTime, expiredTime, alias, masterKey, pwd, lobbyStatus "

    room = str(random.randrange(9999))
    createdTime = '"' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '"'
    expiredTime = '"' + (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S') + '"'
    alias = '"' + str(request.GET['alias']) + '"'
    masterKey = '"' + str(request.GET['key']) + '"'
    pwd = '"' + str(request.GET['pwd']) + '"'
    lobbyStatus = str(1)

    valuestr = room + ',' + createdTime + "," + expiredTime + "," + alias + "," \
        + masterKey + "," + pwd + "," + lobbyStatus

    cursor.execute("insert into v2(" + keystr + ") VALUES(" + valuestr + ");")
    cnx.commit()
    cursor.close()
    cnx.close()
    return render(request, 'room.html')
