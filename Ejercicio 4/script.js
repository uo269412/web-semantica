function ejecutarConsulta() {
  var department = document.getElementById('department').value;
  var addressLocality = document.getElementById('addressLocality').value;

  var prefijos = 'prefix :       <http://example.org/> prefix schema: <http://schema.org/> prefix dbr:    <http://dbpedia.org/resource/>  prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> prefix wdt: <http://www.wikidata.org/prop/direct/>'

  var consulta = prefijos + 'SELECT ?department ?identifier ?legalName ?taxID ?telephone ?email ?status ?streetAddress ?postalCode ?addressLocality WHERE { ?organization a schema:Organization ; schema:department ?department ; schema:identifier ?identifier ; schema:legalName ?legalName ; schema:taxID ?taxID ; schema:telephone ?telephone ; schema:email ?email ; schema:status ?status ; schema:address ?address . ?address a schema:PostalAddress ; schema:streetAddress ?streetAddress ; schema:postalCode ?postalCode ; schema:addressLocality ?addressLocality .';

  if (department !== '') {
    if (addressLocality != '') {
      consulta += ' FILTER(?department = "' + department + '" && ?addressLocality = "' + addressLocality.toUpperCase() + '")';
    } else {
      consulta += ' FILTER(?department = "' + department + '")';
    }

  } else {
    if (addressLocality != '') {
      consulta += ' FILTER(?addressLocality = "' + addressLocality.toUpperCase() + '")';
    } 
  }
  consulta += '}';
  console.log(consulta)

  fetch('http://156.35.98.38:3030/registro-mercantil/sparql', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    },
    body: 'query=' + encodeURIComponent(consulta)
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    mostrarResultados(data);
  })
  .catch(function(error) {
    console.log('Error:', error);
  });
}

function mostrarResultados(data) {
  var resultados = data.results.bindings;
  var resultadoHTML = '';

  for (var i = 0; i < resultados.length; i++) {
    var resultado = resultados[i];
    resultadoHTML += '<article>';
    
    resultadoHTML += '<h2> Resultado número ' + (i+1) + '</h2>'
    for (var variable in resultado) {
      if (resultado.hasOwnProperty(variable)) {
        resultadoHTML += '<p><strong>' + variable + ':</strong> ' + resultado[variable].value + '</p>';
      }
    }

    resultadoHTML += '</article>';
  }


  document.getElementById('resultado').innerHTML = resultadoHTML;
}
