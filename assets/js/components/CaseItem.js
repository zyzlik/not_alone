import React from 'react'
import StageItem from './Stage'


class CaseItem extends React.Component {
    render() {
        let stages = this.props.case.stages.map((stage) => <li key={stage.id}><StageItem stage={stage}/></li>);
        return (
            <div className="box shadow">
                <article className="media">
                    <div className="media-left">
                        <figure className="image is-128x128">
                        <img src={this.props.case.image} alt="Image" className="round"></img>
                        </figure>
                    </div>
                    <div className="media-content">
                        <div>
                        <p>
                            <strong>{this.props.case.title}</strong> <small>{this.props.case.stages.length} steps</small>
                            <br></br>
                            {this.props.case.description}
                        </p>
                        </div>
                    </div>
                </article>
            </div>
        );
    }
}

module.exports = CaseItem