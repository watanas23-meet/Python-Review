def  create_youtube_video(title, descreption,hashtag):
    dict_vid = {"title": title, "descreption": descreption, "likes" : 0, "dislikes" : 0, "conmments" : {"username" : ""}, "hashtag": hashtag }
    return dict_vid 

def likes(vid):
       if likes in vid:
        vid["likes"] = vid["likes"] + 1
        
        return vid

def dislikes(vid):
    if dislikes in vid:
        vid["dislikes"] = vid["likes"] + 1
        
    return vid

def add_comment(youtubevideo, username, comment_text):
    youtubevideo["comments"][username] = comment_text

    return youtubevideo



video = create_youtube_video("NEW HACK FOR ROBLOX!!!! | FREE RUBOX 1M!!!!", "CLICK THE LINK BELOW FRO 100M RUBOX!!!!! : https://sdkjf.asdasdasd/freerubox", {"fun", "roblox", "dada","robux","new"})
video_2 = create_youtube_video("NEW HACK FOR FORTNITE!!!! | FREE VBUCKS 1M!!!!", "CLICK THE LINK BELOW FRO 100M VBUCKS!!!!! : https://sdkjf.asdasdasd/freeFBUCKS", {"fun", "fortnite", "dada","vbucks","new"})

def similarity_to_video(vid1, vid2):
    count = 0
    for i in vid1["hashtag"]:
        for x in vid2["hashtag"]:
            if x == i:
                count = count + 1
    
    result = (count / 5) * 100

    return result


# add 495 likes

for i in 495:
    likes(video)