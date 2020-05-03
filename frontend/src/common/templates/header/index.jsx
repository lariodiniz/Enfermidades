import React from 'react'

import logo from '../../../imgs/logo50.png'

export default props => {
        return (
            <header>
                <nav className="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
                    <a className="navbar-brand col-sm-3 col-md-2 mr-0" href="/">
                        <img className="img-thumbnail" data-test='logo' src={logo} alt="Logo"/>
                            &nbsp; {props.disease}
                    </a>
                </nav>
            </header>
        )
    }
