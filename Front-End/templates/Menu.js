function toggleMenu(menuId) {
    const menu = document.getElementById(menuId);

    // Cierra otros menús abiertos
    document.querySelectorAll('.dropdown-menu').forEach((dropdown) => {
        if (dropdown.id !== menuId) {
            dropdown.style.display = 'none';
        }
    });

    // Alterna la visibilidad del menú seleccionado
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
}

// Cierra el menú desplegable si haces clic fuera de él
document.addEventListener('click', function(event) {
    const isClickInside = event.target.closest('.dropdown');

    if (!isClickInside) {
        document.querySelectorAll('.dropdown-menu').forEach((dropdown) => {
            dropdown.style.display = 'none';
        });
    }
});