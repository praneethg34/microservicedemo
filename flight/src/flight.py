import time
import config
import datetime




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
        self.start = f"{from_city.lower()},{from_state.lower()}"
        self.end= f"{to_city.lower()},{to_state.lower()}"
        self.start_xy= get_lat_long(from_city,from_state)
        self.end_xy=get_lat_long(to_city,to_state)
        self.curr_ind=0
        self.curr_xy=self.start_xy
        self.start_time=None
        self.end_time=None
        self.current_estimate=None

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
                currtime=datetime.datetime.now()
                self.current_estimate=datetime.datetime.strftime((currtime+datetime.timedelta(seconds=((len(self.route)-self.curr_ind)*5))),"%Y-%m-%d %H:%M:%S")
                return self.curr_xy
            except Exception as err:
                self.curr_xy=self.end_xy
                self.status="landed"
                
        return (self.curr_xy)
        


    
              

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
            starttime=datetime.datetime.now()
            self.start_time=datetime.datetime.strftime(starttime,"%Y-%m-%d %H:%M:%S")
            self.end_time=datetime.datetime.strftime((starttime+datetime.timedelta(seconds=(len(self.route)*5))),"%Y-%m-%d %H:%M:%S")
            self.current_estimate=self.end_time


            print(f"{self.flight_number} started flying from {self.start} to {self.end} ")
       
          

                

    




         




