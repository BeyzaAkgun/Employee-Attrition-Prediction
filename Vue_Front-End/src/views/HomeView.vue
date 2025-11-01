<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  // Assuming you're using Bootstrap's jQuery
  $('#customCarousel1').carousel();
});
</script>

<template>
<!--Bunlar koyulcak iloş burda kalsin sürekli bakmayalim.-->
  <!-- Name,Surname,Age,Business Travel,Daily Rate,Department,Distance From Home,Education,Education Field,Employee Number,Environment Satisfaction,
  Gender,Hourly Rate,Job Involvment,Job Level,Job Role,Job Satisfaction,Marial Status,Monthly Income,Monthly Rate,Number of Companies Worked,Over 
  Time,Percent Salary Hike,Performance Rating,Relatisionship Satisfaction,Stock Option Level,Total Working Years,Training Time Last Year,
  Work Life Balance,Years At Company,Years In Current Role,Years Since Last Promotion,Years With Current Manager,Attrition. -->
  <!--Burda sorun su direk css in falan fotosunu koyunca bişi gözükmez çok fazla attribiute var ondan dolayı paragraf olarak bırakıp yanına
   image olarak bırakabiliriz ama ondan da emin olamadim-->
   <!-- slider section -->
   <div class="hero_area" style="overflow: hidden:  !important;;">
   <section class="slider_section ">
      <div id="customCarousel1" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="container ">
              <div class="row">
                <div class="col-md-6">
                  <div class="detail-box">
                    <h1>
                      EMPLOYEE ATTRITION <br>
                      PREDICTING
                    </h1>
                    <p>
                      Welcome to our innovative platform dedicated to transforming how organizations handle employee attrition. At the heart of our service is a predictive approach that empowers businesses to foresee and effectively manage employee turnover. We believe in a threefold strategy: Predict, Prevent, Prosper. By utilizing advanced analytics and insightful data interpretation, we enable companies to predict attrition trends accurately. This foresight allows for proactive measures to prevent unwanted turnover, fostering a more stable and engaged workforce. Our mission is to guide organizations in creating a thriving environment where both employees and employers prosper. Join us in redefining the future of workforce management and take a proactive stance against employee attrition.
                     </p>
                    <!-- <div class="btn-box">
                      
                      <RouterLink class="btn-2" to="/about">Contact Us</RouterLink>
                       Bu button bende bos sayfaya götürüyo.işe yaramıyo. 
                    </div> -->
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="row">
                    <div class=" col-lg-10 mx-auto">
                      <div class="img-box">
                        <img src="../assets/CT/images/slider-img.png" alt="">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="container ">
              <div class="row">
                <div class="col-md-6">
                  <div class="detail-box">
                    <h1>
                      WHY EMPALSIS<br>
                      
                    </h1>
                    <p> <!--Buraya iste yazabiliriz ama cok uzun oluyo-->
                       <!-- Name,Surname,Age,Business Travel,Daily Rate,Department,Distance From Home,Education,Education Field,Employee Number,
                       Environment Satisfaction,Gender,Hourly Rate,Job Involvment,Job Level,Job Role,Job Satisfaction,Marial Status,Monthly Income,
                       Monthly Rate,Number of Companies Worked,Over Time,Percent Salary Hike,Performance Rating,Relatisionship Satisfaction,
                       Stock Option Level,Total Working Years,Training Time Last Year,Work Life Balance,Years At Company,Years In Current Role,
                       Years Since Last Promotion,Years With Current Manager,Attrition.-->
                      </p> 
                    <div class="btn-box">
                      <RouterLink class="btn-2" to="/about">About Us</RouterLink>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="row">
                    <div class=" col-lg-10 mx-auto">
                      <div class="img-box">
                        <img src="../assets/CT/images/slider-img.png" alt="">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- <div class="carousel-item">
            <div class="container ">
              <div class="row">
                <div class="col-md-6">
                  <div class="detail-box">
                    <h1>
                     Excel <br>
                      Format
                    </h1>
                    <p>
                      Your customers are at the heart of your ...
                       </p> -->
                    <!-- <div class="btn-box">
                      <RouterLink class="btn-2" to="/contact">Contact Us</RouterLink>
                    </div> -->
                  <!-- </div>
                </div>
                <div class="col-md-6">
                  <div class="row">
                    <div class=" col-lg-10 mx-auto">
                      <div class="img-box">
                        <img src="../assets/CT/images/slider-img.png" alt="">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div> -->
        </div> 
        <div class="carousel_btn-box">
          <a class="carousel-control-prev" href="#customCarousel1" role="button" data-slide="prev">
            <i class="fa fa-angle-left" aria-hidden="true"></i>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#customCarousel1" role="button" data-slide="next">
            <i class="fa fa-angle-right" aria-hidden="true"></i>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
    </section>
   </div>
    <!-- end slider section -->
  <!-- service section -->

  <!-- <section class="service_section layout_padding">
    <div class="container">
      <div class="heading_container heading_center">
        <h2>
          Our Services
        </h2>
      </div>
    </div>
    <div class="container ">
      <div class="row">
        <div class="col-md-6 col-lg-4 mx-auto">
          <div class="box ">
            <div class="img-box">
              <img src="../assets/CT/images/s4.png" alt="">
            </div>
            <div class="detail-box">
              <h4>
                 Management
              </h4>
              <p>
                Display your ...
              </p>
              <a href="">
                Read More
                <i class="fa fa-long-arrow-right" aria-hidden="true"></i>

              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section> -->

  <!-- end service section -->

  <!-- about section -->

  <!-- <section class="about_section layout_padding-bottom">
    <div class="container  ">
      <div class="row">
        <div class="col-md-6">
          <div class="detail-box">
            <div class="heading_container">
              <h2>
                About Us
              </h2>
            </div>
            <p>
              Welcome to [Your Company Name], where we are committed to understanding and addressing the challenges of employee attrition. 
              Our mission is to empower organizations with valuable insights to 
              foster a positive and thriving workplace environment. </p>
          </div>
        </div>
        <div class="col-md-6 ">
          <div class="img-box">
            <img src="../assets/CT/images/about-img.png" alt="">
          </div>
        </div>

      </div>
    </div>
  </section> -->

  <!-- end about section -->


  <!-- server section -->

  <!-- <section class="server_section">
    <div class="container ">
      <div class="row">
        <div class="col-md-6">
          <div class="img-box">
            <img src="../assets/CT/images/server-img.jpg" alt="">
            
          </div>
        </div>
        <div class="col-md-6">
          <div class="detail-box">
            <div class="heading_container">
              <h2>
                Why Empalsis ?
              </h2>
              <p>
               At [Your Company Name], we are distinguished by our expert team, cutting-edge technology, and a client-centric approach. 
               With deep knowledge in employee engagement, 
               we go beyond standard attrition metrics to offer tailored solutions for a superior employee experience. Our proactive stance on retention, commitment to customization, and dedication to ethical practices set us apart. 
               Choose [Your Company Name] for a results-driven partnership, 
               transforming challenges into opportunities and building a thriving workplace.
              </p>
            </div>
             <RouterLink class="btn-2" to="/contact">Contact Us</RouterLink> 
          </div>
        </div>
      </div>
    </div>
  </section> -->

  <!-- end server section -->

  <!-- price section -->

  <!-- <section class="price_section layout_padding">
    <div class="container">
      <div class="heading_container heading_center">
        <h2 class>
          Our Pricing
        </h2>
      </div>
      <div class="price_container "> -->
        <!--Sildim-->
        <!-- <div class="box">
          <div class="detail-box">
            <h2>$ <span>99</span></h2>
            <h6>
              Standard  -->
              <!--Standart Employee Atrrition-->
              <!--Standart Package-->
            <!-- </h6> -->
            <!--Bu ul yi bastan sona silinebilir ama içine bişi yazmak isteriz diye silmeyip commente aliyorum.-->
            <!-- <ul class="price_features">
              <li>
                4GB RAM
              </li>
              <li>
                50GB SSD Cloud Storage
              </li>
              <li>
                Weekly Backups
              </li>
              <li>
                DDoS Protection
              </li>
              <li>
                Full Root Access
              </li>
              <li>
                24/7/365 Tech Support
              </li>
            </ul> -->
          <!-- </div>
          <div class="btn-box">
            <a href="">
              See Detail
            </a>
          </div>
        </div>
        </div>
      </div>
    
  </section> -->

  <!-- price section -->
   <!--Buraya emin olamadim silip silmemeye direk section taglerinden itibaren tüm section u silersen gidiyo baştan sona silebilirsin istersen.-->
  <!-- client section -->
  <!-- <section class="client_section ">
    <div class="container">
      <div class="heading_container heading_center">
        <h2>
          Testimonial
        </h2>
        <p>
          Streamlining Your ... Operations
        </p>
      </div>
    </div>
    <div class="container px-0">
      <div id="customCarousel2" class="carousel  slide" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="container">
              <div class="row">
                <div class="col-md-10 mx-auto">
                  <div class="box">
                    <div class="img-box">
                      <img src="../assets/CT/images/client.jpg" alt="">
                    </div>
                    <div class="detail-box">
                      <div class="client_info">
                        <div class="client_name">
                          <h5>
                            Morojink
                          </h5>
                          <h6>
                            Customer -->
                          <!-- </h6>
                        </div>
                        <i class="fa fa-quote-left" aria-hidden="true"></i>
                      </div>
                      <p>
                        Switching to Empalsis was a game-changer ...

                        The platform's user-friendly interface allowed us to manage tee times, track member preferences, and communicate effortlessly with our customers. The system's flexibility allowed us to customize our services, making each ...
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="container">
              <div class="row">
                <div class="col-md-10 mx-auto">
                  <div class="box">
                    <div class="img-box">
                      <img src="../assets/CT/images/client.jpg" alt="">
                    </div>
                    <div class="detail-box">
                      <div class="client_info">
                        <div class="client_name">
                          <h5>
                            Morojink
                          </h5>
                          <h6>
                            Customer
                          </h6>
                        </div>
                        <i class="fa fa-quote-left" aria-hidden="true"></i>
                      </div>
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                        labore
                        et
                        dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                        cillum
                        dolore eu fugia
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="container">
              <div class="row">
                <div class="col-md-10 mx-auto">
                  <div class="box">
                    <div class="img-box">
                      <img src="../assets/CT/images/client.jpg" alt="">
                    </div>
                    <div class="detail-box">
                      <div class="client_info">
                        <div class="client_name">
                          <h5>
                            Morojink
                          </h5>
                          <h6>
                            Customer
                          </h6>
                        </div>
                        <i class="fa fa-quote-left" aria-hidden="true"></i>
                      </div>
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                        labore
                        et
                        dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                        cillum
                        dolore eu fugia
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="carousel_btn-box">
          <a class="carousel-control-prev" href="#customCarousel2" role="button" data-slide="prev">
            <i class="fa fa-angle-left" aria-hidden="true"></i>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#customCarousel2" role="button" data-slide="next">
            <i class="fa fa-angle-right" aria-hidden="true"></i>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
    </div>
  </section> -->
  <!-- end client section --> <!--Baştan buraya kadar silinebilir-->

  

  <!-- info section -->

  <!-- <section class="info_section layout_padding2">
    <div class="container">
      <div class="row">
        <div class="col-md-3">
          <div class="info_contact">
            <h4>
              Address
            </h4>
            <div class="contact_link_box">
              <a href="">
                <i class="fa fa-map-marker" aria-hidden="true"></i>
                <span>
                  Istanbul/Turkey
                </span>
              </a>
              <a href="">
                <i class="fa fa-phone" aria-hidden="true"></i>
                <span>
                  Call +01 1234567890
                </span>
              </a>
              <a href="">
                <i class="fa fa-envelope" aria-hidden="true"></i>
                <span>
                  demo@gmail.com
                </span>
              </a>
            </div>
          </div>
          <div class="info_social">
            <a href="">
              <i class="fa fa-facebook" aria-hidden="true"></i>
            </a>
            <a href="">
              <i class="fa fa-twitter" aria-hidden="true"></i>
            </a>
            <a href="">
              <i class="fa fa-linkedin" aria-hidden="true"></i>
            </a>
            <a href="">
              <i class="fa fa-instagram" aria-hidden="true"></i>
            </a>
          </div>
        </div>
        <div class="col-md-3">
          <div class="info_link_box">
            <h4>
              Links
            </h4>
            <div class="info_links">
              <RouterLink to="/">
                <img src="../assets/CT/images/nav-bullet.png" alt="">
                Home
              </RouterLink>
              <RouterLink to="/about">
                <img src="../assets/CT/images/nav-bullet.png" alt="">
                About
              </RouterLink>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <div class="info_detail">
            <h4>
              Info
            </h4>
            <p>
              necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful
            </p>
          </div>
        </div>
        
      </div>
    </div>
  </section> -->

  <!-- end info section -->


  
  <!--footer section-->
<!-- <footer class="footer_section">
    <div class="container">
      <p>
       <span id="displayYear"></span> 
       
      </p>
    </div>
  </footer> -->



</template>
<style scoped>
/* Carousel Button Styles */
.carousel_btn-box {
  position: relative;
  width: 100%;
}

.carousel-control-prev, .carousel-control-next {
  position: absolute;
  top: 500%; /* Align vertically in the middle */
  transform: translateY(-500%); /* Adjust for exact vertical centering */
  font-size: 40px; /* Increase the size of the arrow icons */
  z-index: 5; /* Ensure buttons are above other content */
}

.carousel-control-prev {
  left: 20px; /* Position towards the left */
}

.carousel-control-next {
  right: 20px; /* Position towards the right */
}

/* Font Awesome Icon Adjustments (if needed) */


/* Page Layout Adjustments */
.hero_area {
  min-height: 91vh; /* Set minimum height to full viewport height */
  display: flex;
  flex-direction: column;
  justify-content: center; /* Center content vertically */
  
}

/* Ensure the carousel and its content fit within the viewport */
.slider_section {
  max-height: 100vh; /* Maximum height */
  overflow: hidden; /* Hide any overflowing content */
}

</style>
