import React, { Component }  from 'react'
import Base from '../../common/templates/base'
import Panel from '../../common/templates/panel'
import Loading from '../../common/templates/loading'


import axios from 'axios'
import { constantes } from '../../common/constants'


class Data extends Component {

    constructor(props) {
        super(props)
        this.state = {dados_especificos: {}, mostraGraficos: false}
    }

    _get_dados(){
        axios.get(`${constantes.API_URL}/api/diario`).then((resp) =>{
            this.setState( {...this.state, dados_especificos:resp.data, mostraGraficos:true})
        }).catch(e=>console.log(e))
        console.log('dados atualizados')
        
    }

    _set_continuos_get(){
        setInterval(this._get_dados, 1000);
        
    }

    componentWillMount(){
        this._get_dados()
        this._set_continuos_get()
    }
      

    _format_date(date){

        if (date && date.indexOf("-") !== -1){
            let dateSplit = date.split('-')

            if (dateSplit.length === 3){
                return `${dateSplit[2]}/${dateSplit[1]}/${dateSplit[0]}`
            }
        }

        return date
    }

    _render_table_line(){

        return this.state.dados_especificos.map(dados =>{
            
            return (
                <tr key={dados.pk} className="centraliza_texto">
                    <td >{this._format_date(dados.day)}</td>
                    <td>{dados.infecteds}</td>
                    <td>{dados.infected_porcents}</td>
                    <td>{dados.infected_news}</td>
                    <td>{dados.infected_news_porcents}</td>
                    <td>{dados.deads}</td>
                    <td>{dados.dead_porcents}</td>
                    <td>{dados.dead_news}</td>
                    <td>{dados.dead_news_porcents}</td>
                    <td>{dados.lethality}</td>
                </tr>
            )
        }
        )
        
    }

    _render_table_dados(){
        return (
            <div className="row">
                <div className="col">
                    <h3>Dados Diarios</h3>
                    <div className="table-responsive">
                        <table className="table table-bordered table-striped table-sm">
                            <thead className="thead-dark">
                                <tr>
                                    <th>Dia</th>
                                    <th>Infectados</th>
                                    <th>%</th>
                                    <th>Novos Infectados</th>
                                    <th>%</th>
                                    <th>Mortos</th>
                                    <th>%</th>
                                    <th>Novos Mortos</th>
                                    <th>%</th>
                                    <th>Letalidade</th>
                                </tr>
                            </thead>
                            <tbody>
                                {this._render_table_line()}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        )
    }

    _render_graficos(){
        if (!this.state.mostraGraficos) {
            return <Loading />
        }
        return this._render_table_dados()
    }

    render(){
        return (
            <Base disease="Sars-CoV-2 (Coronavirus)">
                <Panel>
                    {this._render_graficos()}
                </Panel>
            </Base>
        )
    }

}

export default Data