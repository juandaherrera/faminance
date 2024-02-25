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
