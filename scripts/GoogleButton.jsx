import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import { GoogleLogin } from 'react-google-login';
 
 
//const responseGoogle = (response) => {
 // console.log(response);
//}
 
function handleSubmit(event) {
    console.log("reached submit");
    let name = "John Doe"
    Socket.emit('new google user', {
        'name': name,
    });
    console.log('Sent the name '+ name + ' to server!')
}
 
export function GoogleButton() {
    return <GoogleLogin
    clientId="173675092095-ik10csnvu0rqdppgsfoern02eef4vuo0.apps.googleusercontent.com"
    buttonText="Google Login"
    onSuccess={responseGoogle}
    onFailure={responseGoogle}
    cookiePolicy={'single_host_origin'}
  />;
}