from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
import random


def lobby(request):
    cnx = mysql.connector.connect(host='106.14.189.3', port='3306', user='root',\
                                  passwd='L18_jhk123qwe',database='werewolf')
    cursor = cnx.cursor()
    # mysql> create table version-1 ( gameid SMALLINT NOT NULL primarykey ,
    #     -> lobbystatus SMALLINT,
    #     -> playerid SMALLINT,
    #     -> alias varchar(30),
    #     -> role SMALLINT,
    #     -> alive SMALLINT,
    #     -> status SMALLINT,
    #     -> team SMALLINT);

    game1_exist = 0
    #if game1_exist == 0:
    gameid = random.randrange(9999)
    gamestr = "#" + str(gameid)
 #   return render(request, 'lobby.html', {'game1':'value1'},{'game2':'value2'},{'game3':'value3'})
    return render(request, 'lobby.html',{'test': gamestr})

def signin(request):
    return render(request, 'room-sign-in.html')

def create(request):
    cnx = mysql.connector.connect(host='106.14.189.3', port='3306', user='root', \
                                  passwd='L18_jhk123qwe', database='werewolf')
    cursor = cnx.cursor()

    keystr= "gameid, lobbystatus, playerid, alias"
    #gameid = random.random(9999)


    cursor.execute("insert into v1(" + keystr + ") VALUES(" + valuestr + ");")
    cnx.commit()

    cursor.close()
    cnx.close()
    return render(request,'room.html')