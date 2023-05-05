'use strict';
// This works on simple front-end, better use Jquery/TS 
// const warn_txt =   document.querySelector('#txt_demo');
// const loc = document.querySelector('#state');
// const state = document.querySelector('#citycode');
// const phone = document.querySelector('#phone');
// document.getElementById('myBtn').addEventListener('submit', elem => {
//   elem.preventDefault();

//   if (loc.value == "" || state.value == '' || phone.value == "") {
//       loc.focus();
//       state.focus();
//       phone.focus();
//       document.querySelector("#warning").innerText = 'Fill in all fields required!';
//   }
  
//   warn_txt.innerHTML =
//   '<h5>Thank you!</h5><h6>AKA dealers is going to get in touch with you within an hour.</h6>';
//   loc.value = '';
//   state.value = '';
//   phone.value = '';
//   popUp(true);

// });

// const popUp = function (bool) {
//   if (bool) {
//     document.querySelector('#ctc_form').style.visibility = 'visible';
//   } else {
//     document.querySelector('#ctc_form').style.visibility = 'hidden';
//   }
// };


// W3 bg video
// var video = document.querySelector("#myVideo");
// // Get the button
// var btn = document.querySelector("#myBtn");
// // Pause and play the video, and change the button text
// function myFunction() {
//   if (video.paused) {
//     video.play();
//     btn.innerHTML = "Pause";
//     // todo
//   } else {
//     video.pause();
//     btn.innerHTML = "Play";
//   }
// }  


// MUX Video
// POST https://api.mux.com/video/v1/assets
// {
//   "input": "https://storage.googleapis.com/muxdemofiles/mux-video-intro.mp4",
//   "playback_policy": [
//     "public"
//   ]
// }

// Upload video file
// POST https://api.mux.com/video/v1/uploads
// {
//   "new_asset_settings": {
//     "playback_policy": [
//       "public"
//     ]
//   },
//   "cors_origin": "*"
// }