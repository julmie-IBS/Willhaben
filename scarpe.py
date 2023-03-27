import requests

class Willhaben():
    def __init__(self):
        self.string2=[]
        self.r=[]
        self.string=[]
        self.returnlist=[]


    def get_latest_item(self,URL):
        self.returnlist = []
        self.r = requests.get(URL)
        self.string = str(self.r.content)
        self.string2 = self.string.split("<script id=")
        self.string2 = self.string2[1]
        self.string2 = self.string2.split("statusId\":50},\"description\":")
        self.string2.pop(0)
        item=self.string2[0]
        itemnew = item.split("\"")
        print(itemnew[1])
        self.returnlist.append(itemnew[1])

        for idx, (item1) in enumerate(itemnew):
            if "PRICE_FOR_DISPLAY" == item1:
                print(itemnew[idx + 4][13:] + " EURO")
                self.returnlist.append(itemnew[idx + 4][13:] + " EURO")
                pass
        return self.returnlist


    def get_latest_item_v2(self,URL):
        self.returnlist = []
        self.r = requests.get(URL)
        self.string = str(self.r.content)
        self.string2 = self.string.split(":[{\"@type\":\"ListItem\",\"position\":0,\"url\":\"")[1]
        self.string2 = self.string2.split("/\"},{\"@type\":\"ListItem\",\"position\":1")[0]
        print(self.string2)

        return "https://www.willhaben.at/" + self.string2




    def get_all_item(self,URL):
        self.r = requests.get(URL)
        self.string = str(self.r.content)
        self.string2 = self.string.split("<script id=")
        self.string2 = self.string2[1]
        self.string2 = self.string2.split("statusId\":50},\"description\":")
        self.string2.pop(0)
        for item in self.string2:
            itemnew = item.split("\"")
            print(itemnew[1])
            for idx, (item1) in enumerate(itemnew):
                if "PRICE_FOR_DISPLAY" == item1:
                    print(itemnew[idx + 4][13:] + " EURO")
            print("////")







