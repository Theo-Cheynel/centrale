import React from 'react';
import logo from './logo.svg';
import './App.css';
import user from "./user.png";
import clap from "./clap.png";
import superagent from "superagent";

function App() {

	const [movies, setMovies] = React.useState(null);
          React.useEffect(() => 
          {
          superagent.get("http://localhost:5000/application/movie/all").then(response => setMovies(response.body))
            }
            ,[]);


  return (
    <div class="App">
      <header className="App-header">
          

          <img
   	  src={user}
	  className= "App-user"	
	  />	

          <img
   	  src={clap}
	  className= "App-clap"	
	  />



          <div className= "App-font"> 
              <h1> Bondor </h1>
              <p> 
              <h1> Cheynel </h1>
              </p>
          </div>

           <p>

           {movies && movies.map(m => (<div>{m.title} {m.genre}</div>)) }
           </p>
      </header>
    </div>
  );
}

export default App;
