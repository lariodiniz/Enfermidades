import React, { Component }  from 'react'
import { Link } from 'react-router-dom'

import './sidebarMobile.css';





class sidebarMobile extends Component {

    render(){
        return (
            <nav className="navbar navbar-light bg-light">
                <Link className="nav-item nav-link sidebarMobile-nav-item-a" to="/">Index</Link>
                <Link className="nav-item nav-link sidebarMobile-nav-item-a" to="/dados">Dados Diarios</Link>
                <Link className="nav-item nav-link sidebarMobile-nav-item-a" to="/fontes">Fontes</Link>
                <a className="nav-item nav-link sidebarMobile-nav-item-a" target="_blank"  rel="noopener noreferrer" href="http://lariodiniz.com.br/">Quem sou</a>
            </nav>
        )
    }

}

export default sidebarMobile
