class Star_Cinema:
     # Class Attribute 
    __hall_list = []

    def entry_hall(self,hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hallNo) -> None:
        self._rows       = rows
        self._cols       = cols 
        self._hallNo    = hallNo
        self._seats     = {}
        self._show_List = []

        self.my_hall = (rows,cols,hallNo)
        self.entry_hall(self.my_hall)
    
    def entry_show(self,id,movie_Name,time):
        self._id = id
        self._movie_Name = movie_Name
        self._time = time            
        enter_show = (self._id,self._movie_Name,self._time)
        self._show_List.append(enter_show)

        self.seats = [[0 for i in range(self._cols)] for j in range(self._rows)]
        self._seats[self._id] = self.seats #Make a key with id to the attribute seats and value will be the 2d list.

# This work for the Q.No:4

    def book_seats(self,id,seatsForBooking):
        try:
            get = False
            for show in self._show_List:
                if id  == show[0]:
                    get = True
                    break
            if not get:
                raise ValueError("Id not get")
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
        try:
            get = False
            for show in self._show_List:
                if show_id == show[0]:
                    get = True
                    break
            if not get:
                raise ValueError("Id not get for the Show")
            self.BookingId = self._seats[show_id]
            for r in range(0,self._rows):
                for c in range(0,self._cols):
                    print(self.BookingId[r][c],end=' ')
                print()
        except ValueError as e:
            print()
            print(f"Error is : {e} ,  Please Provide valid information \n")


            
        


AnandaCinemaHall  = Hall(8,8,1110)
AnandaCinemaHall.entry_show("101","Buktafitta jay" ,"11.00 AM")
AnandaCinemaHall.entry_show("110","Bedar maye josna","12.00 PM")
AnandaCinemaHall.entry_show("111","Bostir chayle Pocha ", "1.00 Am")
AnandaCinemaHall.entry_show("1000","Murder 2.O ", "2.0 AM")

AnandaCinemaHall.view_available_seats(1010)