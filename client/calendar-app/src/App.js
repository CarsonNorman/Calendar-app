import React, {useState} from 'react';
import Calendar from 'react-calendar';

function App() {
const [date, setDate] = useState(new Date())

  return ( 
    <React.Fragment>
      <h1>React Calendar</h1>
      <div>

      <Calendar onChange={setDate} value={date}/>
      </div>
      <div>
        selected date: {date.toDateString()}
      </div>
    </React.Fragment>
   );
}

export default App;