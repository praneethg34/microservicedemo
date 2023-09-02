import React from 'react';
import { BrowserRouter as Router,Routes, Route} from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store';
import NavBar from './components/NavBar';
import Home from './pages/Home';
import Status from './pages/Status';
import LiveTracking from './pages/LiveTracking';


const App = () => {
  return (
    <Provider store={store}>
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/livetracking" element={< LiveTracking />} />
      </Routes>
    </Router>
    </Provider>
  );
};

export default App;
