
function confirmDelete(id){
    Swal.fire({
        title: "¿Está seguro?",
        text: "No podrá revertir esta acción",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "¡Sí, eliminar!"
        }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
            title: "¡Eliminado!",
            text: "El empleado ha sido eliminado.",
            icon: "success"
            }).then(()=>{
                window.location.href = "/deleteempleado/"+id+"/";
            });
        }
    });
};