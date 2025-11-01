<template>
    <div class="success-download">
      <div class="center-container">
        <div class="header">Successfully Predicted and Downloaded. Please Check Your Downloads Folder</div>
        <div class="header">Attrition Percentage</div>
      </div>
      <div class="progress-circle" :style="circleStyles">
        <span class="percentage">{{ progressPercent }}%</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name:'success',
    data() {
      return {
        progressPercent: null, // Update with your dynamic progress percentage
      };
    },
    mounted() {
    this.fetchStat(); // Call your function here
    },
    computed: {
      circleStyles() {
        return {
          background: `conic-gradient(
            #020230 0% ${this.progressPercent}%, 
            #e0e0e0 ${this.progressPercent}% 100%
          )`,
        };
      },
    },
    methods: {
    async fetchStat() {
        try{
      // Your code to fetch statistics from the backend
     const response = await fetch('http://localhost:5000/statistics')
     if (response.ok) {
      const data = await response.json(); // Parse response JSON
      this.progressPercent = Number(data).toFixed(2); // Assign the response data to progressPercent
    } else {
      throw new Error('Network response was not ok.');
    }
        }
        catch(error) {
          console.error('Error:', error);
        };
    }
  }
  };
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  .success-download {
    display: flex;
    align-items: center; /* Center vertically */
    justify-content: center; /* Center horizontally */
    height: 100vh; /* 100% of viewport height */
    flex-direction: column; /* Stack items vertically */
  }
  
  .center-container {
    text-align: center;
    
  }
  
  .header {
    font-size: 24px;
    margin-bottom: 20px;
    color: blueviolet;
    
  }
  
  .progress-circle {
    position: relative;
    width: 200px; /* Adjust the size of the circle */
    height: 200px; /* Adjust the size of the circle */
    border-radius: 50%;
    overflow: hidden;
    
  }
  
  .percentage {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 24px;
    font-weight: bold;
    color:blueviolet; /* Change the color based on your design */
  }
  </style>