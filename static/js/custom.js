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

// Función específica para formatear números, definida en alguna parte de tu código
function formatNumberInputs(container) {
    $(container)
        .find(".number-format")
        .each(function () {
            // Obtener el valor del input, asumiendo que el separador decimal es un punto.
            var value = $(this).val();

            // Detectar y manejar el signo negativo
            var isNegative = value.startsWith("-");
            if (isNegative) {
                value = value.substring(1);
            }

            // Reemplazar el punto por coma para manejar correctamente los decimales
            // y luego separar la parte entera de los decimales
            var parts = value.split(".");

            // Limpieza de la parte entera: eliminar caracteres no numéricos y ceros a la izquierda innecesarios
            var integerPart = parts[0]
                .replace(/[^\d]/g, "")
                .replace(/^0+/g, "");

            // Añadir separadores de miles a la parte entera
            integerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            // Preparar la parte decimal, si existe, sin cambios adicionales ya que asumimos que era correcta
            var decimalPart = parts.length > 1 ? parts[1] : "";

            // Eliminar ceros finales innecesarios en la parte decimal
            decimalPart = decimalPart.replace(/0+$/, "");

            // Reunir la parte entera y decimal, usando coma como separador decimal si hay parte decimal significativa
            var formattedValue =
                decimalPart.length > 0
                    ? integerPart + "," + decimalPart
                    : integerPart;

            // Reañadir el signo negativo si es necesario
            if (isNegative) {
                formattedValue = "-" + formattedValue;
            }

            // Actualizar el valor del input
            $(this).val(formattedValue);
        });
}

function liveFormatInputNumbers() {
    $(".number-format").on("input", function () {
        // Extraer el valor actual del input
        let value = $(this).val();

        // Eliminar cualquier caracter no numérico excepto la coma
        let cleanValue = value.replace(/[^\d,]/g, "").replace(/^0+/, "");

        // Reemplazar la coma por un punto para el manejo interno como decimal
        let normalizedValue = cleanValue.replace(",", ".");

        // Separar la parte entera de los decimales
        let parts = normalizedValue.split(".");

        // Formatear la parte entera con puntos como separadores de miles
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");

        // Reconstruir el valor con la coma como separador de decimales
        let formattedValue = parts.join(",");

        // Actualizar el valor del input con el valor formateado
        $(this).val(formattedValue);
    });
}

function fixFormatNumbersForBack() {
    $("form").on("submit", function (e) {
        // Encuentra todos los inputs '.number-format' dentro del formulario
        var shouldSubmit = true;
        $(this)
            .find(".number-format")
            .each(function () {
                // Obtiene el valor actual del input, formateado
                let formattedValue = $(this).val();
                // Desformatea el valor para convertirlo a un número estándar
                // Reemplaza puntos por nada y comas por puntos
                let unformattedValue = formattedValue
                    .replace(/\./g, "")
                    .replace(",", ".");

                // Verifica si el valor convertido es numérico
                if (
                    !isNaN(parseFloat(unformattedValue)) &&
                    isFinite(unformattedValue)
                ) {
                    // Actualiza el valor del input con el valor desformateado
                    $(this).val(unformattedValue);
                } else {
                    alert("Por favor, ingrese un número válido.");
                    shouldSubmit = false;
                    return false; // Salir del bucle each
                }
            });

        // Si alguno de los valores no es numérico, prevenir el envío
        if (!shouldSubmit) {
            e.preventDefault();
        }
        // Si todos los valores son numéricos, no se llama a preventDefault, permitiendo el envío del formulario
    });
}

function open_modal(url) {
    $("#default_modal").load(url, function () {
        // $(this).modal({
        //     backdrop: "static",
        //     keyboard: false,
        // });

        $(this).modal("show");
        formatNumberInputs(this);

        liveFormatInputNumbers();
        fixFormatNumbersForBack();
    });

    return false;
}

function close_modal() {
    $("#default_modal").modal("hide");
    return false;
}

function message(title, msg, icon = "success") {
    Swal.fire({
        title: title,
        text: msg,
        icon: icon,
    });
}

function delete_alert(url) {
    Swal.fire({
        title: "Estás seguro?",
        text: "No podrás revertir esta acción!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, bórralo!",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                headers: { "X-CSRFToken": csrfToken },
                type: "POST",
                url: url,
                success: function (response) {
                    console.log(response);
                    if (response.status === "OK") {
                        Swal.fire({
                            title: "Borrado!",
                            text: "La instancia fue borrada con éxito.",
                            icon: "success",
                        }).then((result) => {
                            location.reload(true);
                        });
                    } else {
                        message(
                            "Ups!",
                            "Parace que hubo un error al intentar borrar esta instancia.",
                            "error"
                        );
                    }
                },
            });
        }
    });
}
