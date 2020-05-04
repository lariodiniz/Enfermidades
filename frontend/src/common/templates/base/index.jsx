import React from 'react'

import Header from '../header'
import Sidebar from '../sidebar'
import SidebarMobile from '../sidebarMobile'

import IF from '../../utils/if'

import './base.css';

export default props => {
    
    let isMobile = window.innerWidth <= 575;
    
    return(
    <React.Fragment>

        <Header disease={props.disease} title={props.title}/>
        <div className="container-fluid">
            <div className="row">
                <IF test={!isMobile}>
                     <Sidebar/>
                </IF>
                
                <main role="main" className="col-12 col-sm-10 main">
                    <IF test={isMobile}>
                        <SidebarMobile />
                    </IF>
                    {props.children}
                </main>
            </div>
        </div>
    </React.Fragment>

)
}


