import React, { useEffect, useState } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow, Paper } from '@mui/material';


const convertTime=(timeString)=>{
   

// Get today's date
const date = new Date();

// Extract hours, minutes, and seconds from the time string
const [time, period] = timeString.split(" ");
const [hours, minutes, seconds] = time.split(":").map(Number);

// Convert to 24-hour format
let hours24 = period === "AM" ? hours : hours + 12;

// Special case: 12 AM is 00 in 24-hour time
if (hours === 12 && period === "AM") {
  hours24 = 0;
}

// Special case: 12 PM is 12 in 24-hour time
if (hours === 12 && period === "PM") {
  hours24 = 12;
}

// Set the time on the date object
date.setHours(hours24, minutes, seconds);

return date
}



const FlightTable = ({ flightData }) => {
    const [currentTime, setCurrentTime] = useState(new Date());

    // Update the current time every minute
    useEffect(() => {
      const timer = setInterval(() => {
        setCurrentTime(new Date());
      }, 60000); // 60,000 milliseconds = 1 minute
  
      return () => clearInterval(timer);
    }, [currentTime]);
  return (
    <Paper>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Flight Number</TableCell>
            <TableCell>Origin</TableCell>
            <TableCell>Destination</TableCell>
            <TableCell>Start Time</TableCell>
            <TableCell>End Time</TableCell>
            <TableCell>Current Estimate</TableCell>
            <TableCell>Last Updated</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {flightData.map((flight) => {
            const lastUpdated = convertTime(flight.lastUpdated);
            const timeDifference = Math.abs(currentTime - lastUpdated) / 60000; // in minutes
            const shouldBlink = timeDifference > 1;
            console.log(flight)
            

            return (
              <TableRow key={flight.flightNumber} >
                <TableCell>{flight.flightNumber}</TableCell>
                <TableCell>{flight.origin}</TableCell>
                <TableCell>{flight.destination}</TableCell>
                <TableCell>{flight.startTime}</TableCell>
                <TableCell>{flight.endTime}</TableCell>
                <TableCell>{flight.currentEstimate}</TableCell>
                <TableCell style={{ animation: shouldBlink ? 'blink 1s infinite': 'none'}}>{flight.lastUpdated}</TableCell>
              </TableRow>
            );
          })}
        </TableBody>
      </Table>
    </Paper>
  );
};

export default FlightTable;
