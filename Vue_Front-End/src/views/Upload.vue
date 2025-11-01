<template>
 <!-- <div class="upload-container">
    <input type="file" @change="onFileChange" class="file-input" />
    <button @click="uploadFile" class="upload-button">Upload</button>
  </div> -->
  <div class="format-instructions">
        <p class="format-instructions-text">
          Please ensure your Excel and CSV files adhere to the following format: 
          [Name, Surname, Age, Business Travel, Daily Rate, Department, Distance From Home,
          Education, Education Field, Employee Number, Environment Satisfaction, Gender,
          Hourly Rate, Job Involvement, Job Level, Job Role, Job Satisfaction, Marital Status,
          Monthly Income, Monthly Rate, Number of Companies Worked, Over Time,
          Percent Salary Hike, Performance Rating, Relationship Satisfaction,
          Stock Option Level, Total Working Years, Training Time Last Year, Work Life Balance,
          Years At Company, Years In Current Role, Years Since Last Promotion, Years With Current Manager]
        </p>
      </div>
  <div class="upload-section">
  <div class="upload-container">
    <div class="drop-area" @dragover.prevent @drop="onFileDropE">
      <p class="drag-drop-text">Drag & Drop Excel File Here</p>
      <input type="file" ref="excelFileInput" @change="onFileChangeE" class="file-input" />
      <button @click="openFileInput('excel')" class="browse-button">Browse</button>
      <p v-if="excelfile" class="file-name">{{ excelfile.name }}</p>
    </div>
    <button @click="uploadExcelFile" :disabled="!excelfile" class="upload-button">Upload</button>
    
  </div>
  <div class="upload-container">
    <div class="drop-area" @dragover.prevent @drop="onFileDropC">
      <p class="drag-drop-text">Drag & Drop CSV File Here</p>
      <input type="file" ref="csvFileInput" @change="onFileChangeC" class="file-input" />
      <button @click="openFileInput('csv')" class="browse-button">Browse</button>
      <p v-if="csvfile" class="file-name">{{ csvfile.name }}</p>
    </div>
    <button @click="uploadCsvFile" :disabled="!csvfile" class="upload-button">Upload</button>
    
  </div>
  </div>
  
  </template>
  
  <script>
  import axios from 'axios';
  import { saveAs } from 'file-saver';
  export default {
    methods: {
      onFileChangeE(event) {
        this.excelfile = event.target.files[0];
      },
      onFileChangeC(event) {
        this.csvfile = event.target.files[0];
      },
      onFileDropE(event) {
      event.preventDefault();
      this.excelfile = event.dataTransfer.files[0];
    },
    onFileDropC(event) {
      event.preventDefault();
      this.csvfile = event.dataTransfer.files[0];
    },
    openFileInput(type) {
        if (type === 'excel') {
        this.$refs.excelFileInput.click();
      } else if (type === 'csv') {
        this.$refs.csvFileInput.click();
      }
    },
     async uploadExcelFile() {
      console.log(this.excelfile)
        const formData = new FormData();
        formData.append('file', this.excelfile);
       try{
        // Replace 'API_ENDPOINT' with your actual API endpoint
        const response = await fetch("http://127.0.0.1:5000/upload/excel", {
  method: "POST",
  body: formData,
})
            const rbody = response.body;
            console.log('File uploaded successfully:', rbody);
            // Handle success or perform additional actions
            const blob = await response.blob();
            //saveAs(blob, 'predFileE.xlsx');

const blobURL = URL.createObjectURL(blob);

const link = document.createElement('a');
link.href = blobURL;
link.setAttribute('download', 'predFileE.xlsx');
//link.download = 'predFileE.xlsx'; 
//link.dispatchEvent(new MouseEvent('click'));
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
window.URL.revokeObjectURL(blobURL);

window.location.href = '/success';
          
        }
          catch(error) {
            console.error('Error uploading file:', error);
            alert("Wrong file format.");
            // Handle error or display a message to the user
          }
      },
      
     async uploadCsvFile() {
        const formData = new FormData();
        formData.append('file', this.csvfile);
        try{
        // Replace 'API_ENDPOINT' with your actual API endpoint
       const response = await axios.post('http://127.0.0.1:5000/upload/csv', formData)
          
       const blob = new Blob([response.data]);
            //saveAs(blob, 'predFileE.xlsx');

const blobURL = URL.createObjectURL(blob);


const link = document.createElement('a');
link.href = blobURL;
link.download = 'predFileC.csv'; 
//link.dispatchEvent(new MouseEvent('click'));
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
window.URL.revokeObjectURL(blobURL);
            console.log('File uploaded successfully:', response.data);
            // Handle success or perform additional actions
            window.location.href = '/success';
        }
          catch(error){
            console.error('Error uploading file:', error);
            alert("Wrong file format.");
            // Handle error or display a message to the user
          }
      },
  
    },
    data() {
      return {
        excelfile: null,
        csvfile: null,
      };
    },
  };
  </script>
  <style>
  
  .format-instructions-text {
  text-align: center; /* Center the text */
  margin: 0 auto; /* Center the text box itself */
  max-width: 80%; /* Limit the width of the text box */
  padding: 15px; /* Add some padding inside the box */
  background-color:#020230 ; /* Light background for the text box */
  border: 2px solid white; /* Border to make it distinct */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  white-space: pre-wrap; /* Respect line breaks and spaces */
  color: white;
}
 .upload-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color:#f0f8ff;/* Using the blue background as in other pages */
  color:#fff; /* Adjusting text color for better contrast */
}
  
.upload-container {
  max-width: 600px;
  width: 100%;
  padding: 20px;
  margin: 20px;
  border: 2px solid #007bff;
  border-radius: 10px;
  background-color: #f0f8ff;
}
  
  .drop-area {
    border: 2px dashed #ccc;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 10px;
    background-color: #fff;
    cursor: pointer;
  }
  
  .drop-area:hover {
    border-color: #007bff;
  }
  
  .browse-button,
  .upload-button,
  .download-button {
    margin-top: 10px;
    border: none;
    border-radius: 5px;
    padding: 10px 15px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .browse-button {
    background-color: #007bff;
    color: #fff;
  }
  
  .upload-button {
    background-color: #28a745;
    color: #fff;
  }
  
  .download-button {
    background-color: #17a2b8;
    color: #fff;
  }
  
  .browse-button:hover {
    background-color: #0056b3;
  }
  
  .upload-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .file-input {
    display: none;
  }
  
  .file-name {
    margin-top: 10px;
    font-style: italic;
    color: black;
  }
  .upload-title{
    margin-top: 10px;
    padding-left: 1.5ch;
    font-style: normal;
    color: #0056b3;

  }
  .drag-drop-text {
    color: black; /* Change 'blue' to the desired color */
  }
  </style>