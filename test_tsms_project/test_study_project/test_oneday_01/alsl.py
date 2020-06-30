dcs = {
    "name": "duoceshi",
    "age": "4",
    "grades1": {
        "number": 1,
        #"teachers": ["pansir", "chensir"],
        "students": [{"shenzhen":"xiaohong","guangzhou":"xiaoming", "shanghai":"xiaobai"}],
        "content": "python2"
    },
    "grades2": {
        "number": 2,
        #"teachers": ["pansir", "chensir"],
        "students": [{"shenzhen":"tom","guangzhou": "jerry", "shanghai":"bob"}],
        "content": "python3"
    },
    "grades3": {
        "number": 3,
       # "teachers": ["pansir", "chensir"],
        "students": [{"shenzhen":"阿毛","guangzhou": "阿珍","shanghai": "阿强"}],
        "content": "java"
    }
}

list2=[]
def get2(getkey, res_dict):
     if isinstance(res_dict, dict):
        for k, v in res_dict.items():
            if k == getkey:
                print(v)
                list2.append(v)
            get2(getkey, v)
     if isinstance(res_dict, list):
        for i in res_dict:
            for k, v in i.items():
                if k == getkey:
                    print(v)
                get2(getkey, i)
get2("shenzhen",dcs)
print(list2)