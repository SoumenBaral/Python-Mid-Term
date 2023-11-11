class Star_Cinema:
    def __init__(self) -> None:
        self.hall_list =[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self,row,cal,hallNo) -> None:
        self.row       = row
        self.cal       = cal 
        self.hallNo    = hallNo
        self.seats     = []
        self.show_List = []
    