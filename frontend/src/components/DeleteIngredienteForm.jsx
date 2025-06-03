import React, { useState } from 'react';

const DeleteIngredienteForm = ({ deleteIngrediente }) => {
    const [nombreIngrediente, setingredienteNombre] = useState('');
    
    const handleSubmit = (event) => {
        event.preventDefault();
        if (nombreIngrediente) {
        deleteIngrediente(nombreIngrediente);
        setingredienteNombre('');
        }
    };
    
    return (
        <form onSubmit={handleSubmit}>
        <input
            type="text"
            value={nombreIngrediente}
            onChange={(e) => setingredienteNombre(e.target.value)}
            placeholder="Escribe el Ingrediente a eliminar"
        />
        <button type="submit">Eliminar Ingrediente</button>
        </form>
    );
}

export default DeleteIngredienteForm;