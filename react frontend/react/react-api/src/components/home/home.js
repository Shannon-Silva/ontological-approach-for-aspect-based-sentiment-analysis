import React, { Component } from 'react';
import Main from "../../../src/main.png";
import Second from "../../../src/3.jpg";
import Third from "../../../src/4.png";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';
import './home.css'


export default class Home extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      // <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
      //   <div class="carousel-inner">
      //     <div class="carousel-item active">
      //       <img class="d-block w-100 h-100" src={Main} alt="First slide" />
      //     </div>
      //     <div class="carousel-item">
      //       <img class="d-block w-100 h-100" src={Second} alt="Second slide" />
      //     </div>
      //     <div class="carousel-item">
      //       <img class="d-block w-100 h-100" src={Third} alt="Third slide" />
      //     </div>
      //   </div>
      // </div>

      // <Carousel>
      //           <div>
      //               <img src={Main} />
      //           </div>
      //           <div>
      //               <img src={Second} />
      //           </div>
      //           <div>
      //               <img src={Third} />
      //           </div>
      //       </Carousel>

      <div id = "hero">
        <div id ="hero-overlay"></div>
      </div>
    )
  }
}