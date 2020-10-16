    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

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
    
    getNewMessages();

    return (
        <div>
            <h1>Kash Messenger =)</h1>
                <ol>
                    {messages.map((message, index) =>
                        <li key={index}>{message}</li>)}
                </ol>
            <Button />
        </div>
    );
}
