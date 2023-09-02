import axios from 'axios';


console.log(process.env)
const statusUrl=process.env.REACT_APP_FLIGHT_STATUS_URL
export const fetchFlights = () => {
  return async (dispatch) => {
    dispatch({ type: 'FETCH_FLIGHTS_REQUEST' });
    try {
      console.log(statusUrl)
      const response = await axios.get(statusUrl);
      dispatch({ type: 'FETCH_FLIGHTS_SUCCESS', payload: response.data });
      //dispatch({ type: 'FETCH_FLIGHTS_SUCCESS', payload: testdata });
    } catch (error) {
      dispatch({ type: 'FETCH_FLIGHTS_FAILURE', payload: error });
    }
  };
};
