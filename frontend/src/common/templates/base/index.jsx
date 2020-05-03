import React from 'react'

import Header from '../header'
import Sidebar from '../sidebar'

import './base.css';

export default props => (

    <React.Fragment>

        <Header disease={props.disease} title={props.title}/>
        <div className="container-fluid">
            <div className="row">
                <Sidebar/>
                <main role="main" className="col-12 col-sm-10 main">
                    {props.children}
                </main>
            </div>
        </div>
    </React.Fragment>

)



