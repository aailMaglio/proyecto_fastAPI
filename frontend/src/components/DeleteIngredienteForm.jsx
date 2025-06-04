import React, { useState } from 'react';

const DeleteIngredienteForm = ({ deleteIngrediente }) => {
    const [ingredienteId, setIngredienteId] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        if (ingredienteId) {
            deleteIngrediente(Number(ingredienteId));
            setIngredienteId('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="number"
                value={ingredienteId}
                onChange={(e) => setIngredienteId(e.target.value)}
                placeholder="ID del ingrediente a eliminar"
            />
            <button type="submit">Eliminar Ingrediente</button>
        </form>
    );
};

export default DeleteIngredienteForm;