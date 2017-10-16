import React from 'react'


class StageItem extends React.Component {
    render() {
        return (
            <div>
                <p>{this.props.stage.step_number}. {this.props.stage.title}</p>
                <p>{this.props.stage.body}</p>
            </div>
        );
    }
}

module.exports = StageItem;