from fastapi import FastAPI, HTTPException
from models import flight



app = FastAPI()



@app.get("/flightstatus/")
def read_flights():
    output=flight.get_all_flights()
    if isinstance(output,list):
        return output
    else:
        return {}
    


@app.get("/flightroute/{flight_name}")
def read_flight_route(flight_name: str):

    ft=flight.get_flight(flight_name)
    print(ft)
    if ft:
        flight_number=ft[0].flight_number
        departure_time=ft[0].departure_time

        return flight.get_flight_route(flight_number,departure_time)
    else:
        raise HTTPException(status_code=404, detail="Flight not found")