import axios from 'axios';
import generateTestData from './testdata';

const testdata= generateTestData();
export const fetchFlights = () => {
  return async (dispatch) => {
    dispatch({ type: 'FETCH_FLIGHTS_REQUEST' });
    try {
      //const response = await axios.get('YOUR_API_ENDPOINT_HERE');
      //dispatch({ type: 'FETCH_FLIGHTS_SUCCESS', payload: response.data });
      dispatch({ type: 'FETCH_FLIGHTS_SUCCESS', payload: testdata });
    } catch (error) {
      dispatch({ type: 'FETCH_FLIGHTS_FAILURE', payload: error });
    }
  };
};
