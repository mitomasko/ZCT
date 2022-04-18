def getClass(output):
    output = output.decode("UTF-8").rsplit("Scored Probabilities for Class ")
    
    prediction_class = []
    prediction_acc = []

    for i in range(1, len(output)):
        tmp = output[i]
        prediction_class.append(tmp[2])

        end = tmp.index(",")
        start = tmp.index(":")
        build = ""

        for j in range(start+2, end-1):
            build += tmp[j]
            
        prediction_acc.append(float(build))


    print(prediction_acc)
    print(prediction_class)
    
    acc = max(prediction_acc)
    class_ = prediction_class[prediction_acc.index(acc)]

    return class_, acc

def render_html(spec_class):
    if spec_class == "A":
        return "class_A.html"
    elif spec_class == "B":
        return "class_B.html"
    elif spec_class == "F":
        return "class_F.html"
    elif spec_class == "G":
        return "class_G.html"
    elif spec_class == "K":
        return "class_K.html"
    elif spec_class == "M":
        return "class_M.html"
    elif spec_class == "O":
        return "class_O.html"
    else:
        return "main.html"
