from datetime import datetime
def solution(m, musicinfos):

    FMT = '%H:%M'

    result = None
    dic = dict()

    for music in musicinfos:

        start, finish, title, sound = music.split(',')
        
        temp = datetime.strptime(finish,FMT) - datetime.strptime(start,FMT)
        play = int(temp.total_seconds()//60)

        sound = sound*(play//len(sound))+sound[:(play%len(sound))]
        dic[sound] = title

    for song in dic.keys():
        if m in song:
            if result == None:
                result = song
            else:
                if len(result) < len(song):
                    result = song

    if result != None:
        return dic[result]
    
    else: return "(None)"