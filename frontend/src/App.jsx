import React from 'react';
import './App.css';
import ListaIngredientes from './components/Ingredientes.jsx';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Lista Ingredientes</h1>
      </header>
      <main>
        <ListaIngredientes />
      </main>
    </div>
  );
};

export default App;