'use strict';
// pagination: true,

$(function () {
  $('#table').bootstrapTable({
    search: true,
    columns: [
      {
        field: 'state',
        title: 'State',
      },
      // {
      //   field: 'full_name',
      //   title: 'Name',
      // },
      // {
      //   field: 'price',
      //   title: 'Item Price',
      // },
    ],
  });
});
