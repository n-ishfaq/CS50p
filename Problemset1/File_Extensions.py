def extensions(e):
    if ".jpg" in e:
        return "image/jpg"
    elif ".jpg" in e:
        return "image/jpg"
    elif ".gif" in e:
         return "image/gif"
    elif ".png" in e:
         return "image/png"
    elif ".pdf" in e:
        return "image/pdf"
    elif ".txt" in e:
        return "imageinfo/txt"
    elif ".zip" in e:
        return "image/zip"
    
    else:
        return "application/pdf"
    



ex=input("Tell the filename")
print(extensions(ex))


