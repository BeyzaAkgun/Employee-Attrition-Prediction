<template>
    <div class="file-details-container">
      <div class="content-section">
        <h1>FILE FORMAT DETAILS</h1>
        <p>Please ensure that the files you upload adhere to the following format. Each attribute should be correctly filled to ensure accurate processing.</p>
       
        <ul class="attribute-list">
          <li><strong>Accepted File Formats:</strong> Excel, CSV</li>
          <li><strong>The Attributes In Order:</strong> Name, Surname, Age, Business Travel, Daily Rate, Department, Distance From Home,
          Education, Education Field, Employee Number, Environment Satisfaction, Gender,
          Hourly Rate, Job Involvement, Job Level, Job Role, Job Satisfaction, Marital Status,
          Monthly Income, Monthly Rate, Number of Companies Worked, Over Time,
          Percent Salary Hike, Performance Rating, Relationship Satisfaction,
          Stock Option Level, Total Working Years, Training Time Last Year, Work Life Balance,
          Years At Company, Years In Current Role, Years Since Last Promotion, Years With Current Manager</li>
          <li><strong>Accepted Inputs For The Specified Attributes:</strong> <br>
          Bussines Travel: Rare, Frequently<br>
          Education: Below College, College, Bachelor, Master, Doctor<br>
          Environment Satisfaction: Low, Medium, High, Very High<br>
          Job Involvement: Low, Medium, High, Very High<br>
          Job Satisfaction: Low, Medium, High, Very High<br>
          Performance Rating: Low, Good, Excellent, Outstanding<br>
          Relationship Satisfaction: Low, Medium, High, Very High<br>
          Work Life Balance: Bad, Good, Better, Best<br>
        </li>
          <!-- Add other attributes with their descriptions here -->
        </ul>
        <div class="example-format-section">
        <li><strong>An Excel Format Example:</strong></li>
        <img src="../assets/CT/images/excel-format.png" alt="Example Excel Format" class="example-format-image">
        <img src="../assets/CT/images/excel-format2.png" alt="Example Excel Format" class="example-format-image">
      </div>
      </div>
    </div>
  </template>

<script>
export default {
  name: 'Details'
  // If you need to include methods, data, computed properties, etc., add them here.
};
</script>


<style scoped>
.file-details-container {
  padding: 0;
  background-color: #f0f8ff; /* Light blue background */
  min-height: 100vh; /* Full viewport height */
  width: 100vw; /* Full viewport width */
  box-sizing: border-box; /* Ensures padding is included in the width */
}

.content-section {
  width: calc(100% - 192px); /* Subtract 96px from both sides */
  margin: 0 auto; /* Center the content section */
  padding: 0 96px; /* 96 pixels (1 inch) padding on the left and right */
  text-align: left; /* Align text to the left */
}

.attribute-list,
.example-format-section {
  padding: 0;
  list-style-type: none;
}

.attribute-list li,
.example-format-section li {
  margin-bottom: 10px;
  font-size: 1.1em;
}

h1 {
  color: #020230; /* Dark blue */
  margin: 20px 0; /* Add some space around the heading */
}

.example-format-image {
  max-width: 100%; /* Full width of the container */
  height: auto; /* Maintain aspect ratio */
  border: 1px solid #ccc;
}
</style>