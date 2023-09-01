import React from 'react';
import FlightTrackerMap from '../components/FlightTrackerMap';
const LiveTracking = () => {
    const flightData = [
        { flightNumber: 'AA101', origin: 'New York', destination: 'London', latitude: 28.5073, longitude: -81.3220 ,route: [[28.4773, -81.3370], [28.4873, -81.3320],[28.4973, -81.3270],[28.5073, -81.3220]] },
        { flightNumber: 'BA202', origin: 'San Francisco', destination: 'Tokyo', latitude: 37.7749, longitude: -122.4194 ,route: [[37.7749, -122.4194], [51.5074, -0.1278]]},
        // ... more flights
      ];
    
      return (
        <div>
          <FlightTrackerMap flightData={flightData} />
        </div>
      );
    };

export default LiveTracking;
