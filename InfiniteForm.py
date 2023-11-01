from PIL import Image
from io import BytesIO
import InfiniteFile
import InfiniteApi


class Evolution_stat:
    def __init__(self):        
        self.current_value = 0.0
        self.session_value = 0.0
    
    def update(self, value):
        self.current_value = value
        self.session_value += value


class Medal:
    def __init__(self,gamertag:str, size:int=96):
        self.list_medals = InfiniteApi.get_last_game_medals_list(gamertag)
        self.gamertag = gamertag
        print(self.list_medals)
        #print(str(self.list_medals))
        if self.list_medals != None:
            self.list_img = []
            for medal in self.list_medals:
                id = medal["id"]
                count = medal["count"]
                InfiniteFile.save_medal_in_local(id,size)
                for i in range(count):
                    self.list_img.append(InfiniteFile.get_medal_from_local(id))

    def retrieve_image(self,size=96):
        count = InfiniteApi.get_last_game_medals_count(self.gamertag)
        if count == 0 or count == None: return None
        width = 8
        result = result = Image.new("RGBA", (width*size, count//width*size+int(count%width!=0)*size))
        temp = 0
        for img in self.list_img:
            result.paste(img,box=(temp%width*size, temp//width*size))
            temp += 1
        bin = BytesIO()
        result.save(bin,format="PNG")
        bin.seek(0)
        return bin
