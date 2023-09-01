const generateTestData = () => {
    const origins = ['New York', 'San Francisco', 'Berlin', 'Tokyo', 'Paris'];
    const destinations = ['London', 'Los Angeles', 'Mumbai', 'Sydney', 'Toronto'];
    const flightNumbers = ['AA101', 'BA202', 'CA303', 'DA404', 'EA505', 'FA606', 'GA707', 'HA808', 'IA909', 'JA010'];
  
    const testData = [];
  
    for (let i = 0; i < 10; i++) {
      const flightNumber = flightNumbers[i];
      const origin = origins[Math.floor(Math.random() * origins.length)];
      const destination = destinations[Math.floor(Math.random() * destinations.length)];
      const startTime = new Date().toLocaleTimeString();
      const endTime = new Date(new Date().getTime() + 2 * 60 * 60 * 1000).toLocaleTimeString(); // 2 hours from now
      const currentEstimate = new Date(new Date().getTime() + (Math.random() * 30 - 15) * 60 * 1000).toLocaleTimeString(); // +/- 15 minutes
      const lastUpdated = new Date(new Date().getTime() - Math.random() * 2 * 60 * 1000).toLocaleTimeString(); // up to 2 minutes ago
  
      testData.push({
        flightNumber,
        origin,
        destination,
        startTime,
        endTime,
        currentEstimate,
        lastUpdated,
      });
    }
  
    return testData;
  };
export default generateTestData;
  
  