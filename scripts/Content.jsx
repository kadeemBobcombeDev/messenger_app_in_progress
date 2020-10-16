    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';
import { User } from './User';

export function Content() {
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('messages received', (data) => {
                console.log("Received messages from server: " + data['allMessages']);
                setMessages(data['allMessages']);
            })
        });
    }
    
    function getCurrentUser(){
        React.useEffect(() => {
            Socket.on('')
        });
        
    }
    getNewMessages();
    
    
         
    return (
        <div>
            <h1>Kash Messenger =)</h1>
            <User />
                <ol>
                    {messages.map((message, index) =>
                        <li key={index}>{message}</li>)}
                </ol>
            <Button />
        </div>
    );
}
