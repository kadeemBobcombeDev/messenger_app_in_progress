import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import { GoogleLogin } from 'react-google-login';
 
 
function handleSubmit(response) {
    console.log(response);
    //let name = "John Doe"
    let name = response.profileObj.name
    Socket.emit('new google user', {
        'name': name,
    });
    console.log('Sent the name '+ name + ' to server!')
}
 
/*export function GoogleButton() {
    return <GoogleLogin
    clientId="173675092095-ik10csnvu0rqdppgsfoern02eef4vuo0.apps.googleusercontent.com"
    buttonText="Google Login"
    onSuccess={responseGoogle}
    onFailure={responseGoogle}
    cookiePolicy={'single_host_origin'}
    //callback={handleSubmit()}
  />;
}*/
export function GoogleButton() {
    return (
        
            <GoogleLogin
            clientId="173675092095-ik10csnvu0rqdppgsfoern02eef4vuo0.apps.googleusercontent.com"
            buttonText="Google Login"
            onSuccess={handleSubmit}
            //onFailure={responseGoogle}
            cookiePolicy={'single_host_origin'}
        //callback={handleSubmit()}
            />
            
    );
}