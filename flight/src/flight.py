import time
import config




def get_lat_long(city,state):
    df=config.df
    citi_row=df[df["citistate"]==city.lower()+state.lower()]
    records=citi_row.to_dict('records')
    if records and len(records)>0:
        return (records[0]["lat"],records[0]["lng"])
    else:
        return False    

class Flight():

    def __init__(self,flight_number,from_city,from_state,to_city,to_state):
        self.flight_number="Flight"+flight_number
        self.start = (from_city.lower(),from_state.lower())
        self.end= (to_city.lower(),to_state.lower())
        self.start_xy= get_lat_long(*self.start)
        self.end_xy=get_lat_long(*self.end)
        self.curr_ind=0
        self.curr_xy=self.start_xy
        self.status="landed"


    @property
    def route(self):
        # for simplicity sake, we will use a parabolic equation y=ax2+b
        x1, y1 = self.start_xy
        x2, y2 = self.end_xy
        a=(y1-y2)/(x1**2-x2**2)
        b= y1 - a*x1**2
        route=[]
        xcurr=x1
        if x1 > x2:
            delta=-0.01
        else:
            delta=0.01
        while abs(xcurr-x2) > 0.02:
            ycurr=a*xcurr**2+b
            route.append((xcurr,ycurr))
            xcurr +=delta
        return route 

    
    def get_current_xy(self):
        if self.status=="flying":
            try:
                self.curr_xy=self.route[self.curr_ind]
                self.curr_ind+=1
                return self.curr_xy
            except Exception as err:
                self.curr_xy=self.end_xy
                self.status="landed"
                
        return (self.status,self.curr_xy)
        


    
              

    def take_flight(self):
        if self.status=="landed":
            if self.curr_xy==self.end_xy:
                temp_start=self.start
                temp_startxy=self.start_xy
                self.end=self.start
                self.end_xy=self.start_xy
                self.start=temp_start
                self.start_xy=temp_startxy

            self.status="flying"
            print(f"{self.flight_number} started flying from {self.start} to {self.end} ")
       
          

                

    




         




