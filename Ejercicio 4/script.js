function enviarConsulta() {
    var consulta = $("#query").val();
    console.log(consulta)
    
    // Realiza una petición POST al endpoint SPARQL
    $.ajax({
      url: "http://156.35.98.38:3030/#/dataset/registro-mercantil/query",
      dataType: 'jsonp',
      type: "GET",
      data: {
        query: consulta
      },
      success: function(data) {
        // Muestra el resultado de la consulta en el div de resultado
        $("#resultado").html(data);
      },
      error: function(xhr, status, error) {
        // Manejo de errores
        console.log("Error: " + error);
      }
    });
  }
  