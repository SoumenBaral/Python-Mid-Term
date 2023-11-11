class Star_Cinema:
    def __init__(self) -> None:
        self._hall_list =[]

    def entry_hall(self,hall):
        self._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hallNo) -> None:
        self._rows       = rows
        self._cols       = cols 
        self._hallNo    = hallNo
        self._seats     = {}
        self._show_List = []

        self.my_hall = rows,cols,hallNo
        self.entry_hall(self.my_hall)
    
    def entry_show(self,id,movie_name,time):
        self._id = id 
        self._movie_name = movie_name
        self._time = time 

        movie_info = (id,movie_name,time)
        self.show_List.append(movie_info)

        self.seats =[]
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
            self.seats.append(row)

        self._seats[self._id] = self.seats

    def book_seats(self,id,seatsForBooking):
        try:
            get = False
            for show in self._show_List:
                if id  == show[0]:
                    get = True
                    break
            if get ==True:
                raise ValueError("Id not found")
            for single_set in seatsForBooking:
                row,col = single_set

                if 0<row>self._rows and 0 <col>self._cols:
                    raise ValueError("Invalid Seat ")
                
                self.BookingId = self._seats[id]
                if self.BookingId[row][col] == 1:
                    raise ValueError("This seat already Booked ")
                
                self.BookingId[row][col] = 1

                print("Welcome to our cinematic World,Thank you for Booking")
                print(f"Your Seat Number : {row,col}")

            

        except:       
            print(f'Error is {ValueError} ,  Please Provide valid information')

    def  view_show_list(self):
        for show in self._show_List:
             print(f"\n{show[1]} is Available on ID:({show[0]}) On {show[2]}\n")

    def view_available_seats(self,show_id):
        get = False
        for show in self._show_List:
            if id  == show[0]:
                get = True
                break
        if get ==True:
            raise ValueError("Id not found")
        self.BookingId = self._seats[show_id]
        for r in range (0,self._rows)
        





my_hall2 = Hall(3,3,3232)

hallSets = my_hall2._seats

for set in hallSets:
    print(set)
