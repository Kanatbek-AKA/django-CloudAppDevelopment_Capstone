'use strict';
// 3 steps contact only demo

document.getElementById('btn_demo').addEventListener('click', elem => {
  elem.preventDefault();

  document.querySelector('#txt_demo').innerHTML =
    '<h5>Thank you!</h5><h6>AKA dealers is going to get in touch with you within an hour.</h6>';
  document.querySelector('#loc').value = '';
  document.querySelector('#statecode').value = '';
  document.querySelector('#phone').value = '';
  popUp(true);
});

const popUp = function (bool) {
  if (bool) {
    document.querySelector('#ctc_form').style.visibility = 'visible';
  } else {
    document.querySelector('#ctc_form').style.visibility = 'hidden';
  }
};
