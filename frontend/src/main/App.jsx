import '../common/dependencies'
import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Index from '../views/index'
import Data from '../views/data'
import Font from '../views/fonts'
import NotFound from '../views/notFound'

export default props => (
    <BrowserRouter>
    <Switch>
            <Route path="/" exact={true} component={Index} />
            <Route path="/dados" component={Data} />
            <Route path="/fontes" component={Font} />
            <Route path='*' component={NotFound} />
        </Switch>
    </BrowserRouter>
)
