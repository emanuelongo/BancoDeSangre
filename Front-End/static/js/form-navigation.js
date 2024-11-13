// Toggle display of "cantidad_hijos" field based on selection
function toggleHijosInput() {
    const hijosSelect = document.getElementById("hijos");
    const cantidadHijosContainer = document.getElementById("cantidad_hijos_container");

    if (hijosSelect.value === "si") {
        cantidadHijosContainer.style.display = "block";
    } else {
        cantidadHijosContainer.style.display = "none";
    }
}

// Navegación entre etapas del formulario
let currentStep = 0;
const formSteps = document.querySelectorAll(".form-step");

function showStep(step) {
    formSteps.forEach((stepElement, index) => {
        stepElement.classList.toggle("active", index === step);
    });
}

// Función para pasar a la siguiente etapa
function nextStep() {
    if (currentStep < formSteps.length - 1) {
        currentStep++;
        showStep(currentStep);
    }
}

// Función para volver a la etapa anterior
function prevStep() {
    if (currentStep > 0) {
        currentStep--;
        showStep(currentStep);
    }
}

// Inicializar la primera etapa visible al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    showStep(currentStep);
});
