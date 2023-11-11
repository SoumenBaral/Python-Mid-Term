
class StarCinema:
    # Class Attribute 
    __hall_list = []

    def entry_hall(self,hall):
        self.__hall_list.append(hall)

# This work for the Q.No:2

class Hall(StarCinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []
        
        # Make object of row col and hall_no  and inheritence appned it 
        self.enter_hall = rows,cols,hall_no
        self.entry_hall(self.enter_hall)

# This work for the Q.No:3

    # Make a method in Hall class named entry_show()
    def entry_show(self,id,movie_Name,time):
        self._id = id
        self._movie_Name = movie_Name
        self._time = time            
        enter_show = (self._id,self._movie_Name,self._time)
        self._show_list.append(enter_show)

        self.seats = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self._seats[self._id] = self.seats #Make a key with id to the attribute seats and value will be the 2d list.

# This work for the Q.No:4

    def book_seats(self,show_id, booking_seats):
        try:
            found = False
            for show in self._show_list:
                if show_id == show[0]:
                    found = True
                    break
            if not found:
                raise ValueError("Invalid Id Given for the Show")
            
            for book_single_seat in booking_seats:
                row,col = book_single_seat
                
                if 0 < row > self._rows and 0 < col > self._cols:
                    raise ValueError("InValid Give Seat to Book ")
                
                self.needIdBookSeat = self._seats[show_id]
                if  self.needIdBookSeat[row][col] == 1:
                    raise ValueError("Seat is Booked Already")
                self.needIdBookSeat[row][col] = 1
                
                print(f"\nYour Seat Number{row,col} is booked\n")
        except ValueError as error:
            print(f"\nErro is {error}, Pleas give the right Information\n")
# This work for the Q.No:5
 
    # view_show_list() which will view all the shows running.				
    def view_show_list(self):
        for show in self._show_list:
            print(f"\n{show[1]} is Available on ID:({show[0]}) On {show[2]}\n")

# This work for the Q.No:6
    #  view_available_seats() which will take an id of show, and view the seats that are available in that show
    def view_available_seats(self,show_id):
        try:
            get = False
            for show in self._show_list:
                if id  == show[0]:
                    get = True
                    break
            if get ==True:
                raise ValueError("Id not found")
            self.BookingId = self._seats[show_id]
            for r in range (0,self._rows) :
                for c in range(0,self._cols):
                    print(self.BookingId[r][c],end=' ')
        except ValueError as e:
            print(f"Error is : {e} ,  Please Provide valid information ")


StarCinemaHall = Hall(7,7,1000)
StarCinemaHall.entry_show("001","Avengers EndGame","12:00 AM")
StarCinemaHall.entry_show("002","Avengers Infinity War","1:00 PM")
StarCinemaHall.entry_show("003","Now Here","7:00 AM")
StarCinemaHall.entry_show("004","Jawan","8:00 AM")
StarCinemaHall.view_available_seats(1000)