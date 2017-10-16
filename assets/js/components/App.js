import React from 'react'
import {BrowserRouter as Router, Route} from 'react-router-dom'
import CaseList from './CaseList'


class App extends React.Component {
    render() {
        return (
            <Router>
                <div className='container'>
                    <Route exact path="/" component={CaseList}/>
                </div>
            </Router>
        );
    }
}

module.exports = App;