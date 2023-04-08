"use strict";

// Mozilla JS sample
// // https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
const input = document.querySelector("#image");
const preview = document.querySelector("#preview");
input.style.opacity = 1;
input.addEventListener("change", updateImageDisplay);

function updateImageDisplay() {
  while (preview.firstChild) {
    preview.removeChild(preview.firstChild);
  }
  const curFiles = input.files;
  if (curFiles.length === 0) {
    const para = document.createElement("p");
    para.textContent = "No files currently selected for upload";
    preview.appendChild(para);
  } else {
    const list = document.createElement("ol");
    preview.appendChild(list);
    for (const file of curFiles) {
      const listItem = document.createElement("li");
      const para = document.createElement("p");
      if (validFileType(file)) {
        para.textContent = `File name ${file.name}, file size ${returnFileSize(
          file.size
        )}.`;
        const image = document.createElement("img");
        image.src = URL.createObjectURL(file);

        listItem.appendChild(image);
        listItem.appendChild(para);
      } else {
        para.textContent = `File name ${file.name}: Not a valid file type. Please upload an image.`;
        listItem.appendChild(para);
      }
      list.appendChild(listItem);
    }
  }
}

const fileTypes = [
  "image/apng",
  "image/bmp",
  "image/gif",
  "image/jpeg",
  "image/pjpeg",
  "image/png",
  "image/svg+xml",
  "image/tiff",
  "image/webp",
  "image/x-icon",
];
function validFileType(file) {
  return fileTypes.includes(file.type);
}
function returnFileSize(number) {
  if (number < 1024) {
    return `${number} bytes`;
  } else if (number >= 1024 && number < 1048576) {
    return `${(number / 1024).toFixed(1)} KB`;
  } else if (number >= 1048576) {
    return `${(number / 1048576).toFixed(1)} MB`;
  }
}

//   Alternative
// function validateFileType(){
//     var fileName = document.getElementById("fileName").value;
//     var idxDot = fileName.lastIndexOf(".") + 1;
//     var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
//     if (extFile =="jpg" || extFile=="jpeg" || extFile=="png"){
//         //TO DO
//     }else{
//         alert("Only jpg/jpeg and png files are allowed!");
//     }
