import React from 'react';
import axios from 'axios';

import Forum from '../components/Forum';

class ForumList extends React.Component {

	state = {
		forums: []
	}

	componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/')
      .then(res => {
        console.log(res);
        this.setState({
          forums: res.data
        });
      })
      .catch(err => {
        console.error(err);
      });
  }
  
  render() {
    return (
      <div id="forums-list">
        <Forum data={this.state.forums} />
      </div>
    )
  }
}

export default ForumList;