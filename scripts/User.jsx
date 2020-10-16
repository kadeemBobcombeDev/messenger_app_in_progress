import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let newUser = document.getElementById("user_input");
    Socket.emit('new user input', {
        'user': newUser.value,
    });
    console.log('User: '+ newUser.value +' has entered the chat room.');
    newUser.value = ''
    event.preventDefault();
    
}

export function User(props) {
    
       return (
           <form onSubmit={handleSubmit}>
                {/*<span>You are logged in as: {props.name}</span>*/}
                <input id="user_input" placeholder="Enter your username/nickname"></input>
                <button>Enter</button>
           </form>
        )
}