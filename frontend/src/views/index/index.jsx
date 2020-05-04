import React, { Component }  from 'react'

import axios from 'axios'
import { Chart } from "react-google-charts";


import { constantes } from '../../common/constants'

import Base from '../../common/templates/base'
import Panel from '../../common/templates/panel'
import Loading from '../../common/templates/loading'

var DADOS = {
    'last_update': '00/00/0000',
    'infected': 0,
    'dead': 0,
    'lethality': 0
}

class Index extends Component {

    constructor(props) {
        super(props)
        this.state = {dados_gerais: DADOS, dados_especificos: {}, mostraGraficos: false}
    }

    _get_dados(){
        axios.get(`${constantes.API_URL}/api/totais`).then((resp) =>{
            this.setState( {...this.state, dados_gerais:resp.data})
        }).catch(e=>console.log(e))

        axios.get(`${constantes.API_URL}/api/diario`).then((resp) =>{
            this.setState( {...this.state, dados_especificos:resp.data, mostraGraficos:true})
        }).catch(e=>console.log(e))

    }

    _set_continuos_get(){
        setInterval(this._get_dados(), 30000);
    }

    componentWillMount(){
        this._get_dados()
        //this._set_continuos_get()
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

    _render_dados_gerais(){
        return (
            <div className="row">
                <div className="col">
                    <h3>Dados Totais</h3>
                    <div className="table-responsive">
                        <table className="table table-bordered">
                            <thead className="thead-dark">
                                <tr>
                                    <th>Atualizado</th>
                                    <th>Total de Infectados</th>
                                    <th>Total de Mortos</th>
                                    <th>Letalidade</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr className="table-danger centraliza_texto">
                                    <td>{this._format_date(this.state.dados_gerais.last_update)}</td>
                                    <td>{this.state.dados_gerais.infected}</td>
                                    <td>{this.state.dados_gerais.dead}</td>
                                    <td>{this.state.dados_gerais.lethality} % </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        )
    }

    _render_grafico_totais(){
        let options ={
            title: 'Popoulação Brasileira'
          }

        let data =[
            ['Estatos', 'Quantidade'],
            ['Saldavel', (211462943 - this.state.dados_gerais.infecteds)],
            ['Infectados', this.state.dados_gerais.infecteds],
            ['Mortos', this.state.dados_gerais.deads],
          ]

        return (
            <div className="row">
                <div className="col">
                    <Chart 
                    height={'300px'}
                    chartType="PieChart"
                    data={data}
                    options={options}
                    />
                </div>
            </div>
        )
    }

    _render_grafico_linha(series, data, titleX, titleY){

        let options = {
            series: series,
              lineWidth: 3,
              pointSize: 5,
            hAxis: {
              title: titleX,
              slantedText:true, 
              slantedTextAngle:90,

            },
            vAxis: {
              title: titleY,
            },
          }
          return (
            <div className="row">
                <div className="col">
                    <div className='image'>
                        <Chart 
                        height={'300px'}
                        chartType="LineChart"
                        data={data}
                        options={options}
                        />
                    </div>
                </div>
            </div>
        )
    }

    _render_grafico_dia_infectados(){
        let series = {
            0: { color: '#e2431e' },
            1: { color: '#43459d' }

          }

          let data = [['Dia', 'Infectados', 'Novos Infectados']]

          this.state.dados_especificos.forEach((dados) => {
                let d = [this._format_date(dados.day),dados.infecteds, dados.infected_news]
                data.push(d)
            })

        return this._render_grafico_linha(series, data,'Dia', 'Infectados')
    }

    _render_grafico_dia_mortos(){
        let series = { 0: { color: '#e2431e' },
                       1: { color: '#43459d' }}
          let data = [['Dia', 'Mortos', 'Novos Mortos']]

          this.state.dados_especificos.forEach((dados) => {
                let d = [this._format_date(dados.day),dados.deads, dados.dead_news]
                data.push(d)
            })

        return this._render_grafico_linha(series, data,'Dia', 'Mortos')
    }

    _render_grafico_dia_letalidae(){
        let series = { 0: { color: '#e2431e' }}
          let data = [['Dia', 'Letalidade']]

          
          this.state.dados_especificos.forEach((dados) => {
                let d = [this._format_date(dados.day), Number(dados.lethality)]
                data.push(d)
            })
        
        return this._render_grafico_linha(series, data,'Dia', 'Letalidade')
    }

    _render_grafico_dia_novos_infectados(){
        let series = {
            0: { color: '#e2431e' }
          }

          let data = [['Dia','Novos Infectados']]

          this.state.dados_especificos.forEach((dados) => {
                let d = [this._format_date(dados.day), dados.infected_news]
                data.push(d)
            })

        return this._render_grafico_linha(series, data,'Dia', 'Novos Infectados')
    }

    _render_grafico_dia_novos_mortos(){
        let series = { 0: { color: '#e2431e' }}
          let data = [['Dia',  'Novos Mortos']]

          this.state.dados_especificos.forEach((dados) => {
                let d = [this._format_date(dados.day),dados.dead_news]
                data.push(d)
            })

        return this._render_grafico_linha(series, data,'Dia', 'Novos Mortos')
    }

    _render_graficos(){
        if (!this.state.mostraGraficos) {
            return <Loading />
        }
        return (
            <div className="row">
                <div className="col">
                    {this._render_grafico_totais()}
                    <hr />
                    <h3>Infectados / Dia</h3>
                    {this._render_grafico_dia_infectados()}
                    <hr />
                    <h3>Mortos / Dia</h3>
                    {this._render_grafico_dia_mortos()}
                    <hr />
                    <h3>Letalidade</h3>
                    {this._render_grafico_dia_letalidae()}
                    <hr />                    
                    <h3>Novos Infectados / Dia</h3>
                    {this._render_grafico_dia_novos_infectados()}
                    <hr />                    
                    <h3>Novos Mortos / Dia</h3>
                    {this._render_grafico_dia_novos_mortos()}                                        
                </div>
            </div>
        )
    }

    render(){
        return (
            <Base disease="Sars-CoV-2 (Coronavirus)">
                <Panel>
                    {this._render_dados_gerais()}
                    <hr />
                    {this._render_graficos()}
                </Panel>
            </Base>
        )
    }

}

export default Index