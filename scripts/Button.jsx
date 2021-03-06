import * as React from 'react';
import { Socket } from './Socket';
import { User } from './User';

function handleSubmit(event) {
    let newMessage = document.getElementById("message_input");
    let newUser= document.getElementById("user_input");
    Socket.emit('new message input', {
        'message': newMessage.value,
    });
    
    console.log('Sent the message ' + newMessage.value + ' to server!');
    newMessage.value = ''
    
    event.preventDefault();
}

export function Button() {
    return (
        
        <form onSubmit={handleSubmit}>
            <input id="message_input" placeholder="Enter a new message"></input>
            <button>Send!</button>
        </form>
    ); 
}
