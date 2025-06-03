import React, { useState } from 'react';

const DeleteIngredienteForm = ({ deleteIngrediente }) => {
    const [ingredienteId, setIngredienteId] = useState('');
    
    const handleSubmit = (event) => {
        event.preventDefault();
        if (ingredienteId) {
        deleteIngrediente(ingredienteId);
        setIngredienteId('');
        }
    };
    
    return (
        <form onSubmit={handleSubmit}>
        <input
            type="text"
            value={ingredienteId}
            onChange={(e) => setIngredienteId(e.target.value)}
            placeholder="Escribe el Ingrediente a eliminar"
        />
        <button type="submit">Eliminar Ingrediente</button>
        </form>
    );
}

export default DeleteIngredienteForm;