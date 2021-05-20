function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function onError(error) {
    console.log('Error');
}

async function makeRequest(url, settings) {
    let response = await fetch(url, settings);
    if (response.ok) {
        try{
            return await response.json();
        }
        catch (e) {
            console.log(e)
        }
    } else {
        let error = new Error();
        error.response = response;
        throw error;
    }
}

async function solve(event){
    event.preventDefault();
    let button = event.target;
    let a = document.getElementById('number_1').value;
    let b = document.getElementById('number_2').value;
    let url = button.dataset.url;
    let csrftoken = getCookie('csrftoken');
    try {
        let settings = {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json;charset=utf-8',
                        'X-CSRFToken': csrftoken,
                        },
                        body: JSON.stringify({A: a, B: b}),
        };
        try{
            let data = await makeRequest(url, settings);
            let answer = document.getElementById('answer');
            answer.innerHTML = '<p id="answer" style="color: green">Answer: ' + String(data['answer']) + '</p>';
        }
        catch(error){
            let e = await error.response.json()
            let answer = document.getElementById('answer');
            answer.innerHTML = '<p id="answer" style="color: red">' + e['error'] + '</p>';
        }
    }
    catch(error){
        onError(error);
    }
}

async function onLoad() {
    let url = 'http://localhost:8000/api/get_token/';
    let settings = {method: 'GET'};
    await makeRequest(url, settings);
}

window.addEventListener('load', onLoad);