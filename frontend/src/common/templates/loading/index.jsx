
import React from 'react'
import loading from './loading.gif'

export default props => (
    <div className='image'>
            <img className="img-thumbnail" data-test='loading' src={loading} alt="loading"/>
    </div>
)