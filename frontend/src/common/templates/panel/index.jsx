import React from 'react'

import './panel.css';

export default props => (
        <div className="row panel_div">
            <div className="col">
                {props.children}
            </div>
        </div>
)



