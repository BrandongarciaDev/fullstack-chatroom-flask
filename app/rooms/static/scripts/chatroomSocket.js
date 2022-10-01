const socket = io();




socket.on('connect', function(data){
    console.log('connected')
    socket.emit('chatting', {data});
    socket.emit('load_messages')
})


socket.on('disconnect', function(data){
    socket.emit('chatting', {data});
})


socket.on('chatting', function (data){
    const users = JSON.parse(data);
    const joined = document.getElementById('joined');
    joined.innerHTML = '';
    users.forEach(item =>{
        let user_image = document.createElement('img');
        user_image.src = item.url;
        user_image.id = item.id;
        user_image.classList.add('user__image')
        if (! joined.querySelector("#" + item.id)){
              joined.appendChild(user_image);
        }
    })

})

socket.on('load_messages', function(data){
    const messages = JSON.parse(data);

    const messages_history = document.getElementById("messages__history");

    messages.forEach(message =>{
        let user_message = message.message;
        let created_at = message.created_at;

        let text_message = document.createTextNode(user_message);
        let text_created_at = document.createTextNode(created_at);

        let message_container = document.createElement('div');

        message_container.appendChild(text_message);
        message_container.appendChild(text_created_at);

        messages_history.appendChild(message_container);



    })
})



