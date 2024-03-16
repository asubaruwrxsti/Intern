function submitPostForm() {
    let fname = document.getElementById('fname').value;
    let lname = document.getElementById('lname').value;

    if (fname === '' || lname === '') {
        alert('Please fill in all fields');
    } else {
        let res = fetch('http://localhost:8000/post/form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ fname, lname }),
        });
        res.then((response) => {
            return response.json();
        }).then((data) => {
            alert(data.message);
        });
    }
}

function submitGetForm() {
    let fname = document.getElementById('fname').value;
    let lname = document.getElementById('lname').value;

    if (fname === '' || lname === '') {
        alert('Please fill in all fields');
    } else {
        let res = fetch(`http://localhost:8000/get/form?fname=${fname}&lname=${lname}`);
        res.then((response) => {
            return response.json();
        }).then((data) => {
            alert(data.message);
        });
    }
}
