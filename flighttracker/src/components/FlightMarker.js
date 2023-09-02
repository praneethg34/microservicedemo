
import {  Marker, Popup,Polyline } from 'react-leaflet';
import axios from 'axios';
import { useState,useEffect } from 'react';
import { Icon } from 'leaflet';




const fetchFlightRoute = async (flightNumber) => {
    const routeUrl=process.env.REACT_APP_FLIGHT_ROUTE_URL+flightNumber

    const response = await axios.get(routeUrl);
    const data = response.data;
    

 
    
    return data
}

const getRouteArray = (sortedData)=>{

    const route=[]
    for(var coord in sortedData){
        route.push([sortedData[coord].latitude,sortedData[coord].longitude])
    }
    
   return route


}

const airplane = new Icon({
  iconUrl: "../airplane.png",
  iconSize: [25, 25]
});
const airplane_east = new Icon({
    iconUrl: "../airplane_east.png",
    iconSize: [25, 25]
  });
  const airplane_west = new Icon({
    iconUrl: "../airplane_west.png",
    iconSize: [25, 25]
  });




const FlightMarker = ({flight,index})=>{
    const [routeData,setRouteData]=useState(null)
    const [route,setRoute]=useState([])
    const [flightIcon,setFlightIcon]=useState(airplane)



    useEffect(() => {
        const timer = setInterval(() => {
            
            fetchFlightRoute(flight.flight_number).then((data)=>{setRouteData(data)
              if (routeData!==null && routeData.length > 1){
                routeData[0].latitude >routeData[1].latitude? setFlightIcon(airplane_west):setFlightIcon(airplane_east)
              }
              
            setRoute(getRouteArray(data))})
   
        }, 1000); // 60,000 milliseconds = 1 minute
        
        return () => clearInterval(timer);
      },[routeData]);

   



if (routeData!==null && routeData.length>1){

    
    return(
<Marker key={index} icon={flightIcon} position={[routeData[routeData.length-1].latitude, routeData[routeData.length-1].longitude]}>
<Popup>
  Flight Number: {flight.flight_number}<br />
  Origin: {flight.origin}<br />
  Destination: {flight.destination}<br/>
  Last_updated: {flight.last_updated_time}
</Popup>
<Polyline positions={route} />
</Marker>)
    }
    else{
        return <></>
    }
}

export default FlightMarker