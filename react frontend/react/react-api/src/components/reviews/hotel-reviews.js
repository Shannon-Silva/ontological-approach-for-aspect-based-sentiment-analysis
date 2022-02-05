import React, { Component } from 'react';
import Componentt from '../component1/compo1';
import axios from 'axios';
import { Link } from 'react-router-dom';
import logo from '../../../src/630729-200.png';
import imgg from '../../../src/hotel.jpg'

import { UncontrolledCarousel } from 'reactstrap';
import Main from "../../../src/updated_two.jpg";
import Second from "../../../src/features.png";
import Third from "../../../src/3.jpg";

const Hotel = props => (
  <div className="container">
    <div className="card">
      <div class="card-header">
        <img src={logo} width="40" height="40" class="rounded float-left" />
        <div class="ml-5 pt-2"><h5>Reviewer</h5></div>
      </div>
      <div class="card-body">
        {props.hotel.Comment}
        <br /><br />
        <div class="btn-toolbar float-right mr-3" role="toolbar" aria-label="Toolbar with button groups">
          <div class="btn-group mr-2" role="group" aria-label="First group">
            <a href={"/categorical-analysis/" + props.hotel.table_name + "/" + props.hotel.ID} class="btn btn-primary">Categorical Sentiment</a>
          </div>
          <div class="btn-group mr-2" role="group" aria-label="Second group">
            <a href={"/overall-analysis/" + props.hotel.table_name + "/" + props.hotel.ID} class="btn btn-info">Overall Sentiment</a>
          </div>
        </div>
      </div>
    </div>
    <br />
  </div>
)

export default class HotelReviews extends Component {
  constructor(props) {
    super(props);
    this.state = { hotelrevs: [] }
  }

  componentDidMount() {
    axios.get('http://localhost:5000/hotel')
      .then(response => {
        this.setState({ hotelrevs: response.data.data });
        console.log(this.state.hotelrevs);
      }).catch(err => {
        console.log(err);
      })
  }


  hotelList() {
    return this.state.hotelrevs.map(function (currenthotelrev, i) {
      return <Hotel hotel={currenthotelrev} key={i} />;
    });
  }

  render() {
    return (
      <div style={{ marginTop: 38 }}>
        <div>
          <img src={imgg} width="100%" height="700" />
          <br />
          <br />
          <br/>
        </div>
        <div class="container">
          <div class="row">
            <div class="col-md-20 mx-auto">
              <div class="container">
                {this.hotelList()}
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}