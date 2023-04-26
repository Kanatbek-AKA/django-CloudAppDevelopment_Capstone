'use strict';
// pagination: false,

$(function () {
  $('#tbl').bootstrapTable({
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

