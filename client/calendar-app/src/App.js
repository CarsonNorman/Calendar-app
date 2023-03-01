import React, { useState, useEffect } from 'react';
import axios from 'axios';
function App() {

  const [days, setDays] = useState()
  useEffect(() =>{
    axios.get("http://localhost:5000/days")
    .then(res =>{
      setDays(res.data.days)
      console.log(res.data.days)
    })
  }, [])
  return ( 
    <React.Fragment>
      {days && days.map((day, idx) =>{
        return <h4 key={idx}>{day}</h4>
      })}
    </React.Fragment>
   );
}

export default App;