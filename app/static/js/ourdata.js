$(function() {
  $.getJSON("/datatable", function(some_data) {
    $("#planets_data").DataTable({
      data: some_data,
      columns: [
        { data: "pl_name", title: "Planet Name" },
        { data: "pl_hostname", title: "Host Star" },
        { data: "st_teff", title: "Star Temp (K)" },
        { data: "st_logg", title: "Star Gravity" },
        { data: "pl_eqt", title: "Planet Temp (K)" },
        { data: "st_mass", title: "Star Mass" },
        { data: "st_rad", title: "Star Radius" }
      ]
    });
  });
});