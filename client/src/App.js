import React from 'react';
import logo from './logo.svg';
import './App.css';
import user from "./user.png";

function App() {
  return (
    <div class="App">
      <header className="App-header">
        <div className="carre">

        
          <h1 className="App-title">MOVIESTAR </h1>
       

        <img
   	 src={user}
	 className= "App-user"
		
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
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </div>
      </header>
    </div>
  );
}

export default App;
