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
          <ul className="App-bar">
             <li><a href="default.asp">Home</a></li>
             <li><a href="news.asp">Movies</a></li>
             <li><a href="contact.asp"> TOP 50</a></li>
             <li><a href="about.asp">About</a></li>
          </ul>
        
          <h1 className="App-title">MOVIESTAR </h1>
          

          

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
       
	  <div className= "App-searchbar">
               
                        <font size="5">What would you like to search?</font>
                <form action="" class="formulaire">
               <input class="champ" type="text" value="Search...)"/>
                    <input class="bouton" type="button" onclick = "rechercher()" value="rechercher " />
                    
                </form>
                </div>

           <p className= "App-listmovies">

           {movies && movies.map(m => (<div>{m.title} {m.genre} {m.date}</div>))  }
           </p>
      </header>
    </div>
  );
}

export default App;
