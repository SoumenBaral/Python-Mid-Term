class Star_Cinema:
    def __init__(self) -> None:
        self.hall_list =[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,row,cal,hallNo) -> None:
        self.row       = row
        self.cal       = cal 
        self.hallNo    = hallNo
        self.seats     = []
        self.show_List = []

        self.my_hall = row,cal,hallNo
        self.entry_hall(self.my_hall)
    
    def entry_show(self,id,movie_name,time):
        self.id = id 
        self.movie_name = movie_name
        self.time = time 

        movie_info = (id,movie_name,time)
        self.show_List.append(movie_info)
