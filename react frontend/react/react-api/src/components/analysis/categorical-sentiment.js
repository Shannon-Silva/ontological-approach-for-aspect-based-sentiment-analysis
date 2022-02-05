import React, { Component } from 'react';
import Componentt from '../component1/compo1';
import axios from 'axios';
import logo from '../../../src/630729-200.png';


export default class CategoricalSentiment extends Component {
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
    axios.get('http://localhost:5000/' + this.props.match.params.domain + "/" + this.props.match.params.id)
      .then(res => {
        console.log(this.props)
        this.setState({
          comment: res.data,
          chartData: res.data.chartData,
          review: res.data.comment
        });
        // this.getChartData();
        console.log(this.state);
        // console.log(this.state.text)
      })
  }

  componentWillMount() {
    this.getChartData();
  }
  getChartData() {
    // Ajax calls here
    this.setState({
      chartData: {
        labels: ["Category1", "Category2", "Category3", "Category4"],
        datasets: [
          {
            label: "Red",
            backgroundColor: "#d2222d",
            data: [0, 0, 0, 0]
          }, {
            label: "Yellow",
            backgroundColor: "#ffbf00",
            data: [0, 0, 0, 0]
          },
          {
            label: "Green",
            backgroundColor: "#238823",
            data: [0, 0, 0, 0]
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
            <h5>Reviewer feedback Categorically</h5>
            <div class="ml-5 mr-5 pb-1">
              <Componentt chartData={this.state.chartData} comment={this.state.comment} location="Category One" legendPosition="top" />
            </div>
          </div>

        </div>
        <div className="container">
          <br />
          <br />
        </div>
      </div>
    )
  }
}