import React from 'react'

import Base from '../../common/templates/base'
import Panel from '../../common/templates/panel'


export default props => {

        const cardFont = (titulo, subtitulo, descricao, link) => {
            return (
                <div className="card">
                    <h5 className="card-header">{titulo}</h5>
                    <div className="card-body">
                        <h5 className="card-title">{subtitulo}</h5>
                        <p className="card-text">{descricao}</p>
                        <a href={link} className="btn btn-primary"  target="_blank"  rel="noopener noreferrer">Acessar</a>
                    </div>
                </div>

            )
        }

        return (
            <Base disease="Sars-CoV-2 (Coronavirus)">
                <Panel>
                    <div className="row">
                        <div className="col">
                            <h1>Fontes</h1>
                            <hr />
                            {cardFont('Ministério da Saúde',
                                      'Painel Coronavírus',
                                      `Painel de casos de doença pelo coronavírus 2019 (COVID-19) no Brasil pelo Ministério da Saúde.`,
                                       'https://covid.saude.gov.br/')}
                            <br />
                            {cardFont('Globo', 
                                      'Portal Bem está da Globo', 
                                      `Bem Estar – Notícias, fotos e vídeos sobre saúde e bem-estar`,
                                       'https://g1.globo.com/bemestar/')}
                        </div>
                    </div>
            </Panel>
            </Base>            
        )
    }
