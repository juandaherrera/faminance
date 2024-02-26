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

function open_modal(url) {
    $("#default_modal").load(url, function () {
        // $(this).modal({
        //     backdrop: "static",
        //     keyboard: false,
        // });

        $(this).modal("show");
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
