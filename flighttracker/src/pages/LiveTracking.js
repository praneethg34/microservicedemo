import React, { useEffect } from 'react';
import FlightTrackerMap from '../components/FlightTrackerMap';
import { useDispatch, useSelector } from 'react-redux';
import { fetchFlights } from '../actions/flightActions';


const LiveTracking = () => {

  const dispatch = useDispatch();
  const { flights, loading, error } = useSelector((state) => state.flights);

  useEffect(() => {
    dispatch(fetchFlights());
  }, [dispatch]);

    
      return (
        <div>
          <FlightTrackerMap flightData={flights} />
        </div>
      );
    };

export default LiveTracking;
