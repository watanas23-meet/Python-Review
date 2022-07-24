def  create_youtube_video(title, descreption):
    dict_vid = {"title": title, "descreption": descreption, "likes" : 0, "dislikes" : 0, "conmments" : {"username" : ""}, }
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

video = create_youtube_video("NEW HACK FOR ROBLOX!!!! | FREE RUBOX 1M!!!!", "CLICK THE LINK BELOW FRO 100M RUBOX!!!!! : https://sdkjf.asdasdasd/freerubox")