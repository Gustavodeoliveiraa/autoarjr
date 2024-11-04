const sidebar = document.querySelector(".sidebar-container");
const pin = document.querySelector(".bi-pin");
const navSide = document.querySelector(".nav-side");

// Função para atualizar o estado da sidebar baseado no localStorage
function updateSidebarState() {
    const isFixed = localStorage.getItem("sidebarFixed") === "true";

    if (sidebar && pin) { // Verifica se os elementos existem
        if (isFixed) {
            sidebar.classList.add("sidebar-fixed", "position-fixed", "display-flex", "position-sticky");
            pin.classList.add("bi-pin-fill");
            pin.classList.remove("bi-pin");
            pin.classList.add("top-10"); // Adiciona top-10 se fixo
        } else {
            sidebar.classList.remove("sidebar-fixed", "position-fixed", "display-flex", "position-sticky");
            pin.classList.remove("bi-pin-fill");
            pin.classList.add("bi-pin");
            pin.classList.remove("top-10"); // Remove top-10 se não fixo
        }
    }
}

// Chama a função ao carregar a página
updateSidebarState();

// Adiciona o evento de clique no ícone pin
if (pin) { // Verifica se o ícone existe
    pin.addEventListener('click', () => {
        const isFixed = sidebar.classList.toggle("sidebar-fixed");
        sidebar.classList.toggle("position-fixed");
        sidebar.classList.toggle("display-flex");
        sidebar.classList.toggle("position-sticky");

        // Alterna o ícone entre o pin preenchido e não preenchido
        pin.classList.toggle("bi-pin-fill");
        pin.classList.toggle("bi-pin");

        // Adiciona ou remove a classe top-10 dependendo do estado da sidebar
        if (isFixed) {
            pin.classList.add("top-10");
        } else {
            pin.classList.remove("top-10");
        }

        // Atualiza o estado no localStorage
        localStorage.setItem("sidebarFixed", isFixed);
    });
}
