import React from 'react';
import { MapContainer, TileLayer, Marker, Popup,Polyline } from 'react-leaflet';

const FlightTrackerMap = ({ flightData }) => {
  return (
    
    <MapContainer scrollWheelZoom={false} doubleClickZoom={false} trackResize={false} center={[37.7749, -100.4194]} zoom={4} style={{ height: "100vh", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {flightData.map((flight, index) => (
        <Marker key={index} position={[flight.latitude, flight.longitude]}>
          <Popup>
            Flight Number: {flight.flightNumber}<br />
            Origin: {flight.origin}<br />
            Destination: {flight.destination}
          </Popup>
          <Polyline positions={flight.route} color="blue" />
        </Marker>
      ))}
    </MapContainer>
   
  );
};

export default FlightTrackerMap;