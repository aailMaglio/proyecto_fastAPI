import React, { useEffect, useState } from 'react';
import api from "../api.js";
import AddIngredienteForm from './AddIngredienteForm.jsx';

const ListaIngredientes = () => {
  const [ingredientes, setIngredientes] = useState([]);

  const fetchingredientes = async () => {
    try {
      const response = await api.get('/ingredientes');
      setIngredientes(response.data.ingredientes);
    } catch (error) {
      console.error("Error al recuperar ingredientes", error);
    }
  };

  const addIngrediente = async (nombreIngrediente) => {
    try {
      await api.post('/ingredientes', { nombre: nombreIngrediente });
      fetchingredientes();  // Refrescar la lista después de añadir
    } catch (error) {
      console.error("Error al añadir el ingrediente", error);
    }
  };

  useEffect(() => {
    fetchingredientes();
  }, []);

  return (
    <div>
      <h2>Lista ingredientes</h2>
      <ul>
        {ingredientes.map((ingrediente, index) => (
          <li key={index}>{ingrediente.nombre}</li>
        ))}
      </ul>
      <AddIngredienteForm addIngrediente={addIngrediente} />
    </div>
  );
};

export default ListaIngredientes;