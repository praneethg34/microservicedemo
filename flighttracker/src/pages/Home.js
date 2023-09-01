import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchFlights } from '../actions/flightActions';
import FlightTable from '../components/FlightTable';

const Home = () => {
  const dispatch = useDispatch();
  const { flights, loading, error } = useSelector((state) => state.flights);

  useEffect(() => {
    dispatch(fetchFlights());
  }, [dispatch]);

  return (
    <div>
      
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error.message}</p>}
    <FlightTable flightData={flights} />
    </div>
  );
};

export default Home;
