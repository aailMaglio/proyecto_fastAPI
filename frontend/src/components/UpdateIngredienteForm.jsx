import React, { useState } from 'react';

const UpdateIngredienteForm = ({ updateIngrediente }) => {
  const [ingredienteId, setIngredienteId] = useState('');
  const [nuevoNombre, setNuevoNombre] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (ingredienteId && nuevoNombre) {
      updateIngrediente(Number(ingredienteId), nuevoNombre);
      setIngredienteId('');
      setNuevoNombre('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={ingredienteId}
        onChange={(e) => setIngredienteId(e.target.value)}
        placeholder="ID del ingrediente a actualizar"
      />
      <input
        type="text"
        value={nuevoNombre}
        onChange={(e) => setNuevoNombre(e.target.value)}
        placeholder="Nuevo nombre del Ingrediente"
      />
      <button type="submit">Actualizar Ingrediente</button>
    </form>
  );
}

export default UpdateIngredienteForm;