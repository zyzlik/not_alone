import React from 'react';
import CaseItem from './CaseItem'


const API = {
    BASE: '/api-v1',
    CASELIST: '/cases'
}


class CaseList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          cases: [],
        };
    }
    fetchData() {
        let url = `${API.BASE}${API.CASELIST}`;
        fetch(url).then((res) => res.json()).then((data) => {
            this.setState({
                cases: data
            });
        }).catch((error) => console.log(error));
    }

    componentWillMount() {
        this.fetchData();
    }

    render() {
        let cases = this.state.cases.map((elem) => (<div key={elem.id} className='column is-half'><CaseItem case={elem} /></div>))
        return (
            <div className='columns is-multiline'>{cases}</div>
        )
    }
}

module.exports = CaseList;