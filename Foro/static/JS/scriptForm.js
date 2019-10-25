(function() {
    var formulario = document.getElementsByName('formulario')[0],
        elementos = formulario.elements,
        boton = document.getElementById("boton");

    var validarNombre = function(e) {
        if (formulario.name.value == 0) {
            alert("Por favor ingrese su Nombre.");
            e.preventDefault();
        }
    };

    var validarEmail = function(e) {
        if (formulario.correo.value == 0 || (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(correo))) {
            alert("El formato del Correo es incorrecto.");
            e.preventDefault();
        }
    };
    var validarUser = function(e) {
        if (formulario.usuario.value == 0) {
            alert("Ingrese un nombre de Usuario");
            e.preventDefault();
        }
    };

    var validarPass1 = function(e) {
        if (formulario.pass1.value <= 8) {
            alert("Ingrese una contraseña correcta, mayor a 8 caracteres.");
            e.preventDefault();
        }
    };

    var validarPass2 = function(e) {
        if (formulario.pass2.value != formulario.pass1.value) {
            alert("Las contraseñas no coinciden.");
            e.preventDefault();
        }
    };


    var validacion = function(e) {
        validarNombre(e);
        validarEmail(e);
        validarUser(e);
        validarPass1(e);
        validarPass2(e);

    };
    formulario.addEventListener("submit", validacion);

}());