import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class CharRow extends Component {
  render () {
    const {name, text} = this.props
    return (<div>{name}: {text}</div>)
  }
}

class App extends Component {
  constructor (props) {
    super(props)

    this.state = {
      history: []
    }

    this.handleClickSubmit = this.handleClickSubmit.bind(this)
  }

  handleClickSubmit (e) {
    let {history} = this.state
    let text = this.refs['user-input'].value

    if ( !text) {
      return
    }

    history.push({
      name: 'User',
      text: text
    })

    this.setState({
      history: history
    })

    this.sendToServer(text)
    this.refs['user-input'].value = "" // clean the input
  }

  sendToServer (text) {
    return fetch(window.CONFS.apiServer+'/speak', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          text: text
        })
      })
      .then((res) => res.json())
      .then((res) => {
        console.log('/speak response', res);
        if (res.status==='OK') {
          let {history} = this.state

          history.push({
            name: 'Robot',
            text: res.data
          })

          this.setState({
            history: history
          })
        }
      })
  }

  render() {
    const {history} = this.state

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>

        <hr/>

        <div>
          {history.map((row, i) => <CharRow key={i} {...row}/>)}
        </div>
        <div>
          <input type="text" ref="user-input"/>
          <button onClick={this.handleClickSubmit}>Send</button>
        </div>

        <hr/>
        <p>
            # Gretting, 哈囉, 你好, Hi, Hey <br/>
            # Bye, 掰掰, 再見, see you, byebye <br/>
        </p>
      </div>
    );
  }
}

export default App;
