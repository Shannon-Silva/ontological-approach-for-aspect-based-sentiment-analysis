import React, { Component } from 'react';
import Componentt from '../component1/compo1';
import axios from 'axios';
import { Redirect } from 'react-router-dom';


export default class Api extends Component {
  constructor(props) {
    super(props);

    this.onChangeText = this.onChangeText.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
    this.state = {
      chartData: {},
      comment: {
        table_name: "Table name"
      },
      text: '',
      overallDate: {},
      lines: [],
      onto: [],
      senti: [],
      topics: [],
      words: [],
    }
  }

  onChangeText = (evt) => {
    this.setState({ text: evt.target.value })
  }

  componentWillMount() {
    this.getChartData();
    // this.getOverallData()
  }

  getChartData() {
    // Ajax calls here
    this.setState({
      chartData: {
        labels: ["Category1", "Category2", "Category3", "Category4"],
        datasets: [
          {
            label: "Green",
            backgroundColor: "#238823",
            data: [0.15, 0.1, 0.1, 0.2]
          }, {
            label: "Yellow",
            backgroundColor: "#ffbf00",
            data: [0.2, 0.1, 0.05, 0.05]
          }, {
            label: "Red",
            backgroundColor: "#d2222d",
            data: [0.05, 0.2, 0.1, 0.7]
          }
        ]
      }
    });
  }

  getOverallData() {
    // Ajax calls here
    this.setState({
      chartData: {
        // labels: ["Category1", "Category2", "Category3", "Category4"],
        datasets: [
          {
            label: "Negative",
            backgroundColor: "#d2222d",
            data: [8]
          },
          {
            label: "Neutral",
            backgroundColor: "#ffbf00",
            data: [5]
          },
          {
            label: "Positive",
            backgroundColor: "#238823",
            data: [5]
          }
        ]
      }
    });
  }

  onSubmit(e) {
    e.preventDefault();

    axios.get('http://127.0.0.1:5000/' + this.state.text).then(res => {
      this.setState({
        comment: res.data,
        chartData: res.data.chartData,
        overallDate: res.data.total.chartData,
        lines: res.data.lines,
        onto: res.data.onto,
        senti: res.data.senti,
        topics: res.data.topics,
        words: res.data.words
        // overallDate: res.data.chartData.             
      });
      // this.getChartData();
      console.log(res);
      // console.log(this.state.text)
    }).catch(err => {
      //the error dialog box
      console.log(err)
    })
  }

  render() {
    return (
      <div style={{ marginTop: 20 }}>
        <br /><br /><br />
        <div className="container">
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <textarea type="text"
                className="form-control"
                style={{ "height": "100px" }}
                value={this.state.text}
                onChange={this.onChangeText}
                placeholder="Enter review here..."
              />
            </div>

            <div className="form-group">
              <input type="submit" value="Analyze" className="btn btn-success float-right" />
            </div>
          </form>
        </div>

        <br /><br /><br />


        <div className="container">
          <h6>Word Tokens: </h6>
          <div className="form-group">
            <textarea type="text"
              className="form-control"
              style={{ "height": "150px" }}
              value={this.state.words}
              // onChange={this.onChangeName}
              placeholder="Word tokens..."
            />
          </div>
          <br />
          <h6>Sub Topics Extracted: </h6>
          <div className="form-group">
            <textarea type="text"
              className="form-control"
              style={{ "height": "150px" }}
              value={this.state.topics}
              // onChange={this.onChangeName}
              placeholder="Sub topics extracted..."
            />
          </div>
          <br />
          <h6>Ontology Domain & Categories: </h6>
          <div className="form-group">
            <textarea type="text"
              className="form-control"
              style={{ "height": "150px" }}
              value={"Domain: " + this.state.onto[0] + ". \nCategories: "+ this.state.onto[1]}
              // onChange={this.onChangeName}
              placeholder="Ontology domain and categories..."
            />
          </div>
          <br />
          <h6>Line Tokens: </h6>
          <div className="form-group">
            <textarea type="text"
              className="form-control"
              style={{ "height": "150px" }}
              value={this.state.lines}
              // onChange={this.onChangeName}
              placeholder="Line tokens..."
            />
          </div>
          <br />
          <h6>Sentimental Analysis: </h6>
          <div className="form-group">
            <textarea type="text"
              className="form-control"
              style={{ "height": "150px" }}
              value={"Negative: " + this.state.senti[0] + "\nNeutral: " +this.state.senti[1] + "\nPositive: " +this.state.senti[2] + "\nOverall: " + this.state.senti[3]}
              // onChange={this.onChangeName}
              placeholder="Sentimental Scores..."
            />
          </div>
        </div>

        <br /><br /><br />

        <div className="container">
          <div className="card" style={{ "padding": "20px" }}>
            <h5>Reviewer feedback Categorically</h5>
            <div class="ml-5 mr-5 pb-1">
              <Componentt chartData={this.state.chartData} comment={this.state.comment} location="Category One" legendPosition="top" />
              <br />
            </div>
          </div>
        </div>

        <br />
        <br />
        <br />

        <div className="container">
          <div className="card" style={{ "padding": "20px" }}>
            <h5>Overall Reviewer's Feedback</h5>
            <div class="ml-5 mr-5 pb-1">
              <Componentt chartData={this.state.overallDate} comment={this.state.comment} location="Category One" legendPosition="top" />
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