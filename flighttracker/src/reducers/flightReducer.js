const initialState = {
    flights: [],
    loading: false,
    error: null,
  };
  
  export default function flightReducer(state = initialState, action) {
    switch (action.type) {
      case 'FETCH_FLIGHTS_REQUEST':
        return { ...state, loading: true };
      case 'FETCH_FLIGHTS_SUCCESS':
        return { ...state, loading: false, flights: action.payload };
      case 'FETCH_FLIGHTS_FAILURE':
        return { ...state, loading: false, error: action.payload };
      default:
        return state;
    }
  }
  