import React, { useEffect, useState } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow, Paper } from '@mui/material';


const convertTime=(timeString)=>{
   

// Get today's date
const date = new Date();

// Extract hours, minutes, and seconds from the time string
const [day, time] = timeString.split(" ");
const [hours, minutes, seconds] = time.split(":").map(Number);
const [year,month,whatDay] = day.split("-").map(Number);

// Convert to 24-hour format


// Set the time on the date object
date.setFullYear(year)
date.setMonth(month-1)
date.setDate(whatDay)
date.setHours(hours, minutes, seconds);

return date
}



const FlightTable = ({ flightData }) => {
    const [currentTime, setCurrentTime] = useState(new Date());

    // Update the current time every minute
    useEffect(() => {
      const timer = setInterval(() => {
        setCurrentTime(new Date());
      }, 1000); // 60,000 milliseconds = 1 minute
  
      return () => clearInterval(timer);
    }, [currentTime]);
  return (
    <Paper className='statusTable'>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Flight Number</TableCell>
            <TableCell>Origin</TableCell>
            <TableCell>Destination</TableCell>
            <TableCell>Start Time</TableCell>
            <TableCell>End Time</TableCell>
            <TableCell>Current Estimate</TableCell>
            <TableCell>On Time</TableCell>
            <TableCell>Last Updated</TableCell>  
          </TableRow>
        </TableHead>
        <TableBody>
          {flightData.map((flight) => {
            const lastUpdated = convertTime(flight.last_updated_time);
            const delayed= convertTime(flight.current_estimate)-convertTime(flight.arrival_time) > 300000 ;
                    
            return (
              <TableRow key={flight.flight_number} >
                <TableCell >{flight.flight_number}</TableCell>
                <TableCell>{flight.origin}</TableCell>
                <TableCell>{flight.destination}</TableCell>
                <TableCell>{flight.departure_time}</TableCell>
                <TableCell>{flight.arrival_time}</TableCell>
                <TableCell>{flight.current_estimate}</TableCell>
                <TableCell className={delayed? "delayed" : "ontime" }>{delayed ? "DELAYED" : "ON TIME"}</TableCell>
                <TableCell >{flight.last_updated_time} </TableCell>
                

              </TableRow>
            );
          })}
        </TableBody>
      </Table>
    </Paper>
  );
};

export default FlightTable;
