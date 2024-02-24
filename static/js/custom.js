function formatNumber(number) {
    // Determinar cuántos decimales tiene el número
    const hasDecimals = number % 1 !== 0;

    const formatter = new Intl.NumberFormat("es-ES", {
        minimumFractionDigits: hasDecimals ? 2 : 0, // Mínimo de dígitos fraccionarios
        maximumFractionDigits: 2, // Máximo de dígitos fraccionarios
    });

    return formatter.format(number);
}

$(document).ready(function () {
    // Iterar sobre todos los contenedores colapsables
    $(".sidebar-dropdown").each(function () {
        // Verificar si este contenedor tiene un enlace activo
        if ($(this).find(".nav-link.active").length > 0) {
            // Expandir este contenedor
            $(this).addClass("show");
            // También puedes querer expandir el padre inmediato si está colapsado
            $(this).parent(".collapse").addClass("show");
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    // Formatear cada celda que tenga la clase 'format-number'
    document.querySelectorAll(".format-number").forEach(function (cell) {
        const number = parseFloat(cell.innerText);
        cell.innerText = formatNumber(number);
    });
});
