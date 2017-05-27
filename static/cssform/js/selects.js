const $ = require('jquery');
const venezuela = require('./venezuela.json');

function ReplaceName(id) {
  $(`#${id}`)
    .replaceWith(
      `<select id=${id} name=${id}></select>`
    );
}

ReplaceName('id_estados');
ReplaceName('id_municipios');
ReplaceName('id_parroquias');

setState();

function handleChange() {
  const state = venezuela.filter(function (item) {
    return item.id_estado === $('#id_estados').find('option:selected').first().data('value');
  })
  setMunicipality(state);
}

function setState() {
  venezuela.forEach(function (state, index) {
    var estado = state.estado;
    $('#id_estados')
      .append(`<option data-value="${index +1}" value="${estado}">${estado}</option>`);
  });
}

function setMunicipality(state) {
  $('#id_municipios').empty();
  const municipalitys = state[0].municipios.forEach(function (municipality, index) {
    $('#id_municipios').append(
      `<option data-value="${index}"
        value="${municipality.municipio}">
        ${municipality.municipio}
      </option>`
    );
  });
  localStorage.setItem('municipio', JSON.stringify(state[0].municipios))
}

function setParish(ev) {
  $('#id_parroquias').empty();
  const municipality = $(ev.target).find('option:selected').first().data('value');
  var municipio = JSON.parse(localStorage.getItem('municipio'));
  municipio[municipality].parroquias.forEach(function (parish, index) {
    $('#id_parroquias')
      .append(`<option data-value="${index}" value="${parish}">${parish}</option>`)
  })
}

$('#id_estados').change(handleChange);
$('#id_municipios').change(setParish);
