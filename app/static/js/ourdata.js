$(function() {
  $.getJSON("/dchartcolumns", function(some_data) {
    $("#planets_data").DataTable({
      data: some_data,
      columns: [
        { data: "pl_eqt", title: "pl_eqt" },
        { data: "st_logg", title: "st_logg" },
        { data: "st_mass", title: "st_mass" },
        { data: "st_teff", title: "st_teff" }
      ]
    });
  });
});
