import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import FlightMarker from './FlightMarker';

const FlightTrackerMap = ({ flightData }) => {
  return (
    
    <MapContainer scrollWheelZoom={false} doubleClickZoom={false} trackResize={false} center={[37.7749, -100.4194]} zoom={5} style={{ height: "100vh", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {flightData.map((flight, index) => (

<FlightMarker flight={flight} />
      ))}
    </MapContainer>
   
  );
};

export default FlightTrackerMap;