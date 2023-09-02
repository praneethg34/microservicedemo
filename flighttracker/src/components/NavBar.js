import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const NavBar = () => {
  return (
    <AppBar position="sticky" className='navbar'>
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          ADP POC 
        </Typography>
        <Button color="inherit" component={Link} to="/">
          Home
        </Button>
        <Button color="inherit" component={Link} to="/livetracking">
          Live Tracking
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
