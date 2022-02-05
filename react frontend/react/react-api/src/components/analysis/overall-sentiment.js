import React, { Component } from 'react';
import Componentt from '../component1/compo1';
import axios from 'axios';
import logo from '../../../src/630729-200.png';


export default class OverallSentiment extends Component {
  constructor(props) {
    super(props);
    this.state = {
      chartData: {},
      comment: {
        table_name: ''
      },
      review: ''
    }
  }

  componentDidMount() {
    // console.log(this.props)
    axios.get('http://localhost:5000/' + this.props.match.params.domain + "/total/" + this.props.match.params.id)
      .then(res => {
        console.log(this.props)
        this.setState({
          comment: res.data,
          chartData: res.data.chartData,
          review: res.data.comment
        });
        // this.getChartData();
        console.log(this.state.chartData);
        // console.log(this.state.text)
      })
  }

  componentWillMount() {
    this.getChartData();
  }

  // getChartData() {
  //   // Ajax calls here
  //   this.setState({
  //     chartData: {
  //       labels: ["Category1", "Category2", "Category3", "Category4"],
  //       datasets: [
  //         {
  //           label: "Green",
  //           backgroundColor: "#238823",
  //           data: [0.15, 0.1, 0.1, 0.2]
  //         }, {
  //           label: "Yellow",
  //           backgroundColor: "#ffbf00",
  //           data: [0.2, 0.1, 0.05, 0.05]
  //         }, {
  //           label: "Red",
  //           backgroundColor: "#d2222d",
  //           data: [0.05, 0.2, 0.1, 0.7]
  //         }
  //       ]
  //     }
  //   });
  // }

  getChartData() {
    // Ajax calls here
    this.setState({
      chartData: {
        // labels: ["Category1", "Category2", "Category3", "Category4"],
        datasets: [
          {
            label: "Negative",
            backgroundColor: "#d2222d",
            data: [0.7]
          },
          {
            label: "Neutral",
            backgroundColor: "#ffbf00",
            data: [0.05]
          },
          {
            label: "Positive",
            backgroundColor: "#238823",
            data: [0.15]
          }
        ]
      }
    });
  }


  render() {
    return (
      <div style={{ marginTop: 20 }}>
        <br /><br />
        <div className="container">
          <h2>Review Analysis...</h2><br />
          <div class="card">
            <div class="card-header">
              <img src={logo} width="40" height="40" class="rounded float-left" />
              <div class="ml-5 pt-2"><h5>User</h5></div>
            </div>
            <div class="card-body">
              {/* <h5 class="card-title">Card title</h5> */}
              <p class="card-text">{this.state.review}</p>
            </div>
          </div>
        </div>

        <br /><br />

        <div className="container">
          <div className="card" style={{ "padding": "20px" }}>
            <h5>Overall Reviewer's Feedback</h5>
            <div  class="ml-5 mr-5 pb-1">
            <Componentt chartData={this.state.chartData} comment={this.state.comment} location="Category One" legendPosition="top" />
            </div>
          </div>

        </div>
        <div className="container">
          <br />
          <br />
          <br />
        </div>
      </div>
    )
  }
}