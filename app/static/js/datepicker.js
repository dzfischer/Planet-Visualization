$(function() {
  $('input[name="dates"]').daterangepicker({
      singleDatePicker: true,
      showDropdowns: true,
      startDate: moment().subtract(1, 'day'),
      minYear: 2016,
      maxDate: moment().subtract(1, 'day')
  })
});
