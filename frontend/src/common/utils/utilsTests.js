import checkPropTypes from 'check-prop-types'
import { applyMiddleware, createStore } from 'redux'
import rootReducer  from '../../main/reducers'
import { middleware } from '../../createStore'

export const findByTestAtrr = (componet, attr) => {

    let findComponent = componet.find(`[data-test='${attr}']`);
    return findComponent;
}

export const checkProps = (componet, expectedProps) => {

    let propsErr = checkPropTypes(componet.propTypes, expectedProps, 'props', componet.name);
    return propsErr;
}

export const testStore = (initialState) => {
    const createStoreWithiddleware = applyMiddleware(...middleware)(createStore);
    
    return createStoreWithiddleware(rootReducer, initialState);
}




