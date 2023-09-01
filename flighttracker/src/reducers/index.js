import { combineReducers } from 'redux';
import flightReducer from './flightReducer';

export default combineReducers({
  flights: flightReducer,
});