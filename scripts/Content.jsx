    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';
import { User } from './User';
/*import { Supreme } from './supremebackground.jpg';*/

export function Content() {
    const [messages, setMessages] = React.useState([]);
    const [users, setUsers] = React.useState([]);


    function getNewMessages() {
        React.useEffect(() => {
            Socket.on('messages received', (data) => {
                console.log("Received messages from server: " + data['allMessages']);
                setMessages(data['allMessages']);
            })
        });
    }
    
    function getNewUsers(){
        React.useEffect(() => {
            Socket.on('users joined', (data) => {
                console.log("Recieved users from server: " + data['allUsers']);
                setUsers(data['allUsers']);
            })
        });
        
    }
    getNewMessages();
    getNewUsers();
    
    
         
    return (
        <div style={{
            position: 'absolute', left: '50%', top: '50%',
            transform: 'translate(-50%, -50%)'
        }}>
            <h1 style= {{ textAlign: "center" }}>Kash Messenger =)</h1>
            
                <div style={{overflow: 'auto', maxHeight: 200}}>
                    <ol>
                        {messages.map((message, index) =>
                            <li key={index}>{message}</li>)}
                    </ol>
                </div>

            <div style={{ textAlign: "center" }}>
                <Button />
            </div>
            <div style={{overflow: 'auto', maxHeight: 200}}>
                <h2 style= {{ textAlign: "center" }}>Current Users</h2>
                <ol>
                    {users.map((user, index) =>
                        <li key={index}>{user}</li>)}
                </ol>
            </div>
        </div>
    );
}