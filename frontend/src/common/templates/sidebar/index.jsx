import React, { Component }  from 'react'
import { Link } from 'react-router-dom'

import './sidebar.css';


class Sidebar extends Component {

    render(){
        return (
            <nav className="col-sm-2 d-none d-sm-block bg-light sidebar">
                <div className="sidebar-sticky">
                    <ul className="nav flex-column sidebar-nav">
                        <li className="nav-item centraliza_texto ">
                            <Link className="nav-link sidebar-nav-item-a" to="/">Index</Link>
                            
                        </li>
                        <li className="nav-item centraliza_texto">
                            <Link className="nav-link sidebar-nav-item-a" to="/dados">Dados Diarios</Link>
                        </li>
                    </ul>
                    <h6 className="centraliza_texto">Desenvolvedor</h6>
                    <ul className="nav flex-column mb-2">
                        <li className="nav-item centraliza_texto">
                            <a className="nav-link  sidebar-nav-item-a" target="_blank"  rel="noopener noreferrer" href="http://lariodiniz.com.br/">Lário Diniz</a>
                        </li>
                    </ul>
                </div>
            </nav>
        )
    }

}

export default Sidebar
