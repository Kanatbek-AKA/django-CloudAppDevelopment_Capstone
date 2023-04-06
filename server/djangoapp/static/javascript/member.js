const input = document.querySelector('#input');
const preview = document.querySelector('#preview');

input.style.opacity = 0;

input.addEventListener('change', updateImageDisplay);

function updateImageDisplay() {
    while(preview.firstChild) {
      preview.removeChild(preview.firstChild);
    }
    const curFiles = input.files;
    if (curFiles.length === 0) {
      const para = document.createElement('p');
      para.textContent = 'No files currently selected for upload';
      preview.appendChild(para);
    } else {
      const list = document.createElement('ol');
      preview.appendChild(list);
      for (const file of curFiles) {
        const listItem = document.createElement('li');
        const para = document.createElement('p');
        if (validFileType(file)) {
          para.textContent = `File name ${file.name}, file size ${returnFileSize(file.size)}.`;
          const image = document.createElement('img');
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

//   Alternative 
// // https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
// const fileTypes = [
//     "image/apng",
//     "image/bmp",
//     "image/gif",
//     "image/jpeg",
//     "image/pjpeg",
//     "image/png",
//     "image/svg+xml",
//     "image/tiff",
//     "image/webp",
//     "image/x-icon"
//   ];
  
//   function validFileType(file) {
//     return fileTypes.includes(file.type);
//   }
  
// // 
// function validateFileType(){
//     var fileName = document.getElementById("fileName").value;
//     var idxDot = fileName.lastIndexOf(".") + 1;
//     var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
//     if (extFile =="jpg" || extFile=="jpeg" || extFile=="png"){
//         //TO DO
//     }else{
//         alert("Only jpg/jpeg and png files are allowed!");
//     }   