import React, { useState } from 'react';

const AddIngredienteForm = ({ addIngrediente }) => {
  const [ingredienteNombre, setingredienteNombre] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (ingredienteNombre) {
      addIngrediente(ingredienteNombre);
      setingredienteNombre('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={ingredienteNombre}
        onChange={(e) => setingredienteNombre(e.target.value)}
        placeholder="Escribe el Ingrediente"
      />
      <button type="submit">Añade Ingrediente</button>
    </form>
  );
};

export default AddIngredienteForm;