function copyToClipboard(id) {
    const copyText = document.getElementById(id);
  
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
    navigator.clipboard.writeText(copyText.value);
}

document.onpaste = function(event) {
    // TODO flash loading message

    const textarea = document.querySelector('#detected-text');
    const reader = new FileReader();

    const items = event.clipboardData.items;

    for(let item of items) {
        if(['image/png', 'image/jpeg'].includes(item.type)) {
            const blob = item.getAsFile();
            if(blob) {
                reader.onload = function(event) {
                    console.log(event.target.result);
                    axios
                        .post('/', {
                            image: event.target.result
                        })
                        .then(res => textarea.innerHTML = res.data.text);
                };
                reader.readAsDataURL(blob);
                break;
            }
        }
    }
}
