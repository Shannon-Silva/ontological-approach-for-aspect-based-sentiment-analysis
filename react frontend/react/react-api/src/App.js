import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import './App.css';
// import logo from '../src/logo 01.png';
import logo from '../src/logo_final white.png';
import "bootstrap/dist/css/bootstrap.min.css"

import Api from './components/api/api';
import Home from './components/home/home';
import Hotel from './components/reviews/hotel-reviews';
import Movie from './components/reviews/movie-reviews';
import CategoricalSentiment from './components/analysis/categorical-sentiment';
import OverallSentiment from './components/analysis/overall-sentiment';
import Home1 from './components/home/home1';

function App() {
  return (
    <Router>
      <div className='App-component'>
        <nav className="navbar fixed-top navbar-expand-lg navbar-dark bg-dark" style={{ "height": "55px" }}>
          <a className="nav-brand justify-content-start" href="/">
            <img src={logo} width="215" height="50" alt="" padding="0 px" />
            <Link to="/" className="navbar-brand ml-3 pt-3" ></Link>
            {/* <h6>API for Ontology based Sentiment Analysis</h6> */}
          </a>
          <div className="collpase navbar-collapse justify-content-end">
            <ul className="justify-content-end nav">
              <li className="nav-item">
                <Link to={'/api'} className="nav-link" style={{ "color": "white" }}>Demo</Link>
              </li>
              <li className="nav-item">
                <Link to={'/movie'} className="nav-link" style={{ "color": "white" }}>Movie Reviews</Link>
              </li>
              <li className="nav-item">
                <Link to={'/hotel'} className="nav-link" style={{ "color": "white" }}>Hotel Reviews</Link>
              </li>
            </ul>
          </div>
        </nav>
        <hr />
        <Switch>
          <Route exact path='/' component={Home1} />
          <Route exact path='/api' component={Api} />
          <Route path='/hotel' component={Hotel} />
          <Route path='/home' component={Home} />
          <Route path='/movie' component={Movie} />
          <Route path='/categorical-analysis/:domain/:id' component={CategoricalSentiment} />
          <Route path='/overall-analysis/:domain/:id' component={OverallSentiment} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
