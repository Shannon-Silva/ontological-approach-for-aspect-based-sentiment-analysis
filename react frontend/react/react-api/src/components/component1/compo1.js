import React, { Component } from 'react';
import { Bar } from 'react-chartjs-2';

class Home extends Component {
  constructor(props) {
    super(props);
    // this.state = {
    //   chartData: props.chartData,
    // }
  }
  static defaultProps = {
    displayTitle: true,
    displayLegend: true,
    legendPosition: 'right',
    location: 'Category'
  }
  render() {
    return (
      <div>
        <div>
          <div className="chart">
            <Bar
              height={100}

              data={this.props.chartData}
              options={{
                title: {
                  display: this.props.displayTitle,
                  text: this.props.comment.table_name,
                  fontSize: 20
                },
                legend: {
                  display: this.props.displayLegend,
                  position: this.props.legendPosition
                }
              }}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default Home;