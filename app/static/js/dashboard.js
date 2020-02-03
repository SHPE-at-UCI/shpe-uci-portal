
// This updates the name of the file in the resume file input
// whenever the user changes the file to upload
// TODO: require a pdf only
// TODO: upload to backend
function updateFilename() { 
    let fileName = document.getElementById('resumeUpload').value;
    console.log(fileName);
    let splitPath = fileName.split("\\");
    document.getElementById('resumeLabel').innerHTML = splitPath[splitPath.length - 1];
}