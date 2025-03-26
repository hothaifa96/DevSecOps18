import React, { Component } from 'react';

class Biggy extends Component {
    state = { 
        styles :[{
            width: '150px',
            height: '50px'
         },
         {
            width: '300px',
            height: '100px'
         },
         {
            width: '450px',
            height: '150px'
         }
        ]
        ,
        index:0

     } 
     
    render() { 
        return (
            <button className='btn btn-success m-3' 
            style={this.state.styles[this.state.index]}
            onClick={(ev)=>this.changeSize(ev)} > FeedMe </button>
            
        );
    }

    changeSize=(ev)=>{
        if(this.state.index < 2)
            this.state.index++;
        else{
            ev.target.innerHTML='Im curvy and i like it';
        }
        this.setState({index: this.state.index})
    }
}
 
export default Biggy;