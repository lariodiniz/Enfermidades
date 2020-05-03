import React from 'react'

import imgagemEscolhida from './404.png'

export default props => (

    <div className="container">
        <br />
        <div className="row"> 
            <div className='col'>
                <div className="row justify-content-md-center">
                    <img className="img-fluid rounded" alt="mostra 404 not found" src={imgagemEscolhida}/>
                </div>
            </div>
        </div>
    </div>
)



